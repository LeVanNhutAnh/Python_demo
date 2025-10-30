from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
import os
import io
import tempfile
import PyPDF2
import docx
from docx import Document
from openai import OpenAI
import google.generativeai as genai
from dotenv import load_dotenv

# Load biến môi trường từ file .env
load_dotenv()

# Cấu hình OpenAI client - đọc từ biến môi trường
client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

# Cấu hình Google Gemini - đọc từ biến môi trường
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
gemini_model = genai.GenerativeModel('gemini-flash-latest')

def generate_smart_demo_response(message, action_type):
    """Generate intelligent demo responses when AI APIs are unavailable"""
    message_lower = message.lower()
    
    if action_type == 'translate':
        if any(word in message_lower for word in ['xin chào', 'chào', 'hello']):
            return "Hello! Nice to meet you!"
        elif any(word in message_lower for word in ['cảm ơn', 'thank']):
            return "Thank you very much!"
        else:
            return f"English translation: This is a demo translation of your Vietnamese text. For accurate translation, please add your Google AI Studio API key."
    
    elif action_type == 'summarize':
        return f"Tóm tắt thông minh: Văn bản của bạn ({len(message)} ký tự) có chủ đề chính là giao tiếp và tương tác. Các điểm quan trọng đã được trích xuất và tóm gọn."
    
    elif action_type == 'improve':
        if len(message) < 50:
            return f"Văn bản cải thiện: {message.capitalize()}. (Đã cải thiện cấu trúc và ngữ pháp)"
        else:
            return f"Văn bản của bạn đã được cải thiện về mặt ngữ pháp, từ vựng và cấu trúc câu. Nội dung trở nên rõ ràng và chuyên nghiệp hơn."
    
    else:  # question
        if any(word in message_lower for word in ['xin chào', 'hello', 'hi']):
            return "Xin chào! Tôi là trợ lý AI thông minh. Tôi có thể giúp bạn trả lời câu hỏi, dịch thuật, tóm tắt và cải thiện văn bản. Bạn cần tôi giúp gì?"
        elif any(word in message_lower for word in ['cảm ơn', 'thank']):
            return "Rất vui được giúp đỡ bạn! Nếu cần hỗ trợ thêm, đừng ngần ngại hỏi nhé."
        elif any(word in message_lower for word in ['bạn là ai', 'who are you']):
            return "Tôi là trợ lý AI được tích hợp vào ứng dụng Speech-to-Text này. Tôi có thể giúp bạn xử lý văn bản một cách thông minh!"
        else:
            return f"Tôi hiểu bạn đang hỏi về: '{message[:50]}...'. Đây là câu trả lời thông minh từ hệ thống demo AI. Để có phản hồi chính xác từ AI thật, vui lòng thêm API key cho OpenAI hoặc Google Gemini."

# Create your views here.
def home(request):
    """Main home page with Speech to Text interface"""
    return render(request, 'home.html')

def extract_text_from_pdf(file_content):
    """Extract text from PDF file"""
    try:
        pdf_file = io.BytesIO(file_content)
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        
        text = ""
        page_count = len(pdf_reader.pages)
        
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
            
        return text.strip(), page_count
    except Exception as e:
        raise Exception(f"Lỗi đọc file PDF: {str(e)}")

def extract_text_from_docx(file_content):
    """Extract text from DOCX file"""
    try:
        doc_file = io.BytesIO(file_content)
        doc = Document(doc_file)
        
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
            
        # Count pages (approximate based on content length)
        page_count = max(1, len(text) // 2000)  # Rough estimate
        
        return text.strip(), page_count
    except Exception as e:
        raise Exception(f"Lỗi đọc file Word: {str(e)}")

def extract_text_from_doc(file_content):
    """Extract text from older DOC format (fallback method)"""
    try:
        # This is a simplified extraction - for production use python-docx2txt or other libraries
        return "Nội dung file DOC đã được trích xuất (demo)", 1
    except Exception as e:
        raise Exception(f"Lỗi đọc file DOC: {str(e)}")

@csrf_exempt
def analyze_document(request):
    """Analyze uploaded Word/PDF documents"""
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    if 'file' not in request.FILES:
        return JsonResponse({'error': 'Không có file được upload'}, status=400)
    
    try:
        uploaded_file = request.FILES['file']
        file_name = uploaded_file.name
        file_size = uploaded_file.size
        
        # Read file content
        file_content = uploaded_file.read()
        
        # Extract text based on file type
        file_extension = file_name.lower().split('.')[-1]
        
        if file_extension == 'pdf':
            extracted_text, page_count = extract_text_from_pdf(file_content)
        elif file_extension == 'docx':
            extracted_text, page_count = extract_text_from_docx(file_content)
        elif file_extension == 'doc':
            extracted_text, page_count = extract_text_from_doc(file_content)
        else:
            return JsonResponse({'error': 'Định dạng file không được hỗ trợ'}, status=400)
        
        if not extracted_text.strip():
            return JsonResponse({'error': 'Không thể trích xuất văn bản từ file'}, status=400)
        
        # Count words
        word_count = len(extracted_text.split())
        
        # Detect language (simple detection)
        vietnamese_chars = "àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđ"
        is_vietnamese = any(char in vietnamese_chars for char in extracted_text.lower())
        language = "Tiếng Việt" if is_vietnamese else "English/Other"
        
        # AI Analysis - truncate text if too long
        analysis_text = extracted_text[:3000] if len(extracted_text) > 3000 else extracted_text
        
        try:
            # Try OpenAI first
            analysis_prompt = f"""Hãy phân tích tài liệu sau và cung cấp:
1. Chủ đề chính
2. Các điểm quan trọng 
3. Cấu trúc nội dung
4. Đánh giá tổng quan

Văn bản: {analysis_text}"""

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": analysis_prompt}],
                max_tokens=800,
                temperature=0.7
            )
            ai_analysis = response.choices[0].message.content
            
            # Summary
            summary_prompt = f"Hãy tóm tắt nội dung chính của tài liệu sau bằng tiếng Việt (3-5 câu): {analysis_text}"
            
            summary_response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": summary_prompt}],
                max_tokens=300,
                temperature=0.5
            )
            summary = summary_response.choices[0].message.content
            
        except Exception as openai_error:
            # Fallback to Gemini
            try:
                analysis_prompt = f"Phân tích tài liệu này và đưa ra nhận xét về nội dung, cấu trúc và ý nghĩa: {analysis_text}"
                gemini_response = gemini_model.generate_content(analysis_prompt)
                ai_analysis = gemini_response.text
                
                summary_prompt = f"Tóm tắt ngắn gọn nội dung chính: {analysis_text}"
                summary_response = gemini_model.generate_content(summary_prompt)
                summary = summary_response.text
                
            except Exception as gemini_error:
                # Demo fallback
                ai_analysis = f"""Phân tích demo cho tài liệu "{file_name}":
                
🎯 Chủ đề chính: Tài liệu có vẻ chứa nội dung về [chủ đề được phát hiện từ nội dung]

📋 Các điểm quan trọng:
- Văn bản có cấu trúc rõ ràng với {word_count} từ
- Nội dung được trình bày một cách có hệ thống
- Ngôn ngữ sử dụng: {language}

📊 Cấu trúc: Tài liệu gồm {page_count} trang với nội dung được tổ chức logic

✅ Đánh giá: Tài liệu có giá trị thông tin và dễ đọc hiểu"""

                summary = f"Tóm tắt: Đây là một tài liệu {page_count} trang chứa {word_count} từ, được viết bằng {language}. Nội dung tập trung vào các khái niệm và thông tin chuyên môn quan trọng."
        
        return JsonResponse({
            'success': True,
            'file_name': file_name,
            'file_size': file_size,
            'word_count': word_count,
            'page_count': page_count,
            'language': language,
            'ai_analysis': ai_analysis,
            'summary': summary,
            'extracted_text_preview': extracted_text[:500] + "..." if len(extracted_text) > 500 else extracted_text
        })
        
    except Exception as e:
        return JsonResponse({
            'error': f'Lỗi khi phân tích tài liệu: {str(e)}'
        }, status=500)

@csrf_exempt
def whisper_transcribe(request):
    """Transcribe audio using OpenAI Whisper API"""
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    if 'audio' not in request.FILES:
        return JsonResponse({'error': 'Không có file audio'}, status=400)
    
    temp_file_path = None
    try:
        audio_file = request.FILES['audio']
        language = request.POST.get('language', 'vi')
        
        # Validate file size (max 25MB for Whisper API)
        if audio_file.size > 25 * 1024 * 1024:
            return JsonResponse({'error': 'File audio quá lớn (max 25MB)'}, status=400)
        
        # Check if OpenAI client is properly configured
        if not hasattr(client, 'audio'):
            return JsonResponse({
                'error': 'OpenAI client không được cấu hình đúng. Fallback về demo mode.',
                'transcription': f'[Demo] Bạn đã nói bằng tiếng {language}. Để sử dụng Whisper thật, cần API key hợp lệ.',
                'engine': 'Demo Mode'
            })
        
        # Create a temporary file for the audio
        with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as temp_file:
            for chunk in audio_file.chunks():
                temp_file.write(chunk)
            temp_file_path = temp_file.name
        
        # Validate temp file exists and has content
        if not os.path.exists(temp_file_path) or os.path.getsize(temp_file_path) == 0:
            return JsonResponse({'error': 'File audio không hợp lệ'}, status=400)
        
        # Call Whisper API with error handling
        try:
            with open(temp_file_path, 'rb') as audio_file_obj:
                # Add timeout and better error handling
                response = client.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file_obj,
                    language=language if language != 'vi' else None,  # Whisper uses 'auto' for Vietnamese
                    response_format="text",
                    timeout=30
                )
            
            # Extract text from response
            transcription_text = str(response).strip()
            
            if not transcription_text:
                transcription_text = "[Không nhận dạng được âm thanh]"
            
            return JsonResponse({
                'success': True,
                'transcription': transcription_text,
                'language': language,
                'engine': 'OpenAI Whisper'
            })
            
        except Exception as whisper_error:
            error_msg = str(whisper_error)
            
            # Handle specific OpenAI errors
            if 'quota' in error_msg.lower():
                demo_text = f"[Demo - Hết quota] Bạn vừa nói bằng {language}. Whisper API đã hết quota."
            elif 'api_key' in error_msg.lower() or 'authentication' in error_msg.lower():
                demo_text = f"[Demo - Lỗi API] API key không hợp lệ. Bạn vừa ghi âm bằng {language}."
            elif 'timeout' in error_msg.lower():
                demo_text = f"[Demo - Timeout] Whisper API timeout. Bạn vừa ghi âm bằng {language}."
            else:
                demo_text = f"[Demo - Lỗi khác] {error_msg[:50]}... Bạn vừa ghi âm bằng {language}."
            
            return JsonResponse({
                'success': True,  # Return success to avoid breaking UI
                'transcription': demo_text,
                'language': language, 
                'engine': 'Demo Mode (Whisper unavailable)',
                'original_error': error_msg
            })
            
    except Exception as e:
        return JsonResponse({
            'error': f'Lỗi hệ thống: {str(e)}',
            'transcription': f'[Demo] Lỗi không xác định. Bạn vừa ghi âm.',
            'success': True  # Graceful fallback
        })
    
    finally:
        # Always clean up temp file
        if temp_file_path and os.path.exists(temp_file_path):
            try:
                os.unlink(temp_file_path)
            except:
                pass  # Ignore cleanup errors

@csrf_exempt
def ai_chat(request):
    """Handle AI chat requests with OpenAI"""
    if request.method == 'POST':
        try:
            import json
            # Xử lý encoding cho tiếng Việt
            data = json.loads(request.body.decode('utf-8'))
            user_message = data.get('message', '')
            action_type = data.get('type', 'question')
            
            if not user_message:
                return JsonResponse({
                    'error': 'Không có nội dung để xử lý'
                }, status=400)
            
            # Tạo prompt tùy theo loại action
            if action_type == 'translate':
                prompt = f"Translate the following Vietnamese text to English: {user_message}"
            elif action_type == 'summarize':
                prompt = f"Summarize the following text in Vietnamese: {user_message}"
            elif action_type == 'improve':
                prompt = f"Improve the following Vietnamese text (fix grammar, enhance vocabulary, better structure): {user_message}"
            elif action_type == 'punctuation':
                prompt = f"Fix punctuation, capitalization, and sentence structure for this Vietnamese text. Only return the corrected text without explanations: {user_message}"
            else:  # question
                prompt = f"Answer this question in Vietnamese: {user_message}"
            
            # Thử OpenAI trước, nếu lỗi thì dùng Gemini
            try:
                # Gọi OpenAI API với syntax v1+
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=500,
                    temperature=0.7
                )
                ai_response = response.choices[0].message.content
                ai_provider = "OpenAI GPT-3.5"
                
            except Exception as openai_error:
                # Nếu OpenAI lỗi, dùng Google Gemini
                try:
                    gemini_response = gemini_model.generate_content(prompt)
                    ai_response = gemini_response.text
                    ai_provider = "Google Gemini"
                except Exception as gemini_error:
                    # Nếu cả 2 đều lỗi, dùng smart demo response
                    ai_response = generate_smart_demo_response(user_message, action_type)
                    ai_provider = "Smart Demo (AI unavailable)"
            
            return JsonResponse({
                'success': True,
                'response': ai_response,
                'type': action_type,
                'provider': ai_provider
            })
            
        except Exception as e:
            return JsonResponse({
                'error': f'Lỗi khi gọi AI: {str(e)}'
            }, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)


def chat_demo(request):
    """Render the chat demo page (GPT-style mock)"""
    return render(request, 'chat_demo.html')
