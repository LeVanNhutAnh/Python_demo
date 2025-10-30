# Chương 2: Cơ sở lý luận và phương pháp nghiên cứu

## 2.1. Cơ sở lý luận

### 2.1.1. X[?25l[?25h[?25lX[?25hử lý ngôn ngữ tự nhiên (NLP)

NLP là lĩnh vực giúp máy tính hiểu, phân tích và sinh văn bản giống con người. Các nhiệm vụ chính: tokenization (tách từ), NER (nh[?25l[?25h[?25lận dạng thực thể), sentiment analysis (ph[?25l[?25h[?25hl[?25hẩm t[?25hực), machine translation (dịch máy), text summarization (t[?25hóm t[?25ham), question answering (hỏi đáp). 

Đề tài ứng dụng NLP qua API của OpenAI (GPT-3.5) và Google (Gemini) để thực hiện tóm tắt, dịch, cải thiện văn bản và hỏi đáp theo ngữ cảnh.

### 2.1.2. Mô hình ngôn ng[?25hl[?25hm lớn (LLMs)

LLMs là các mô hình deep learning được huấn luyện trên khối lượng lớn dữ liệu văn bản để học các quy luật ngôn ngữ và tri thức thế giới.

#### a) Kiến tr[?25hl trúc Transformer
Transformer (Vaswani et al., 2017) là nền tảng của hầu hết LLMs hiện đại, gồm hai cơ chế chính:
- Self-Attention Mechanism (Scaled Dot-Product Attention): Cho phép mô hình "ch[?25hlu ý" đến các phần khác nhau của input để hiểu ngữ cảnh. Công thức: Attention(Q,K,V) = softmax(QK^T/√d_k)V, trong đó Q (query), K (key), V (value) là các ma trận biểu diễn input, d_k là chiều của key vector, việc chia cho √d_k giúp ổn định gradient.
- Positional Encoding: Mã hóa vị trí từ trong câu vì Transformer không có khái niệm thứ tự tự nhiên.
- Cấu trúc: Encoder (xử lý input) + Decoder (sinh output). GPT sử dụng kiến trúc Decoder-only (autoregressive), BERT sử dụng Encoder-only (bidirectional).

#### b) Pre-training và Fine-tuning
- Pre-training: Học unsupervised trên dữ liệu lớn thông qua các nhiệm vụ như next-token prediction.
- Fine-tuning: Tinh chỉnh supervised trên dữ liệu nhỏ có nhãn cho task cụ thể.
- Few-shot Learning: Các LLMs hiện đại (GPT-3, GPT-4) có khả năng học từ vài ví dụ (few-shot) hoặc không cần ví dụ (zero-shot) thông qua prompt engineering.

#### c) LLMs sử dụng trong đề tài
- OpenAI GPT-3.5 Turbo: Dịch vụ chat của OpenAI, tối ưu về chi phí và tốc độ, phù hợp cho các tác vụ hội thoại, tóm tắt và dịch thuật.
- Google Gemini: Mô hình multimodal (xử lý text, image, audio), có gói miễn phí, được sử dụng làm fallback cho GPT-3.5.

### 2.1.3. Speech-to-Text (STT)

STT là công nghệ chuyển đổi giọng nói thành văn bản, qua quy trình: Feature Extraction (MFCC, mel-spectrogram) 123→ Acoustic Model (ánh xạ sang phonemes) → Language Model (dự đoán chuỗi từ).

#### a) OpenAI Whisper
Whisper là mô hình STT mã nguồn mở của OpenAI, hỗ trợ 99 ngôn ngữ với độ chính xác cao:
- Kiến trúc: Encoder-Decoder Transformer.
- Huấn luyện: 680,000 giờ audio đa dạng (podcast, video, audiobook).
- Chức năng: Transcription (chuyển giọng nói thành văn bản), translation (dịch sang tiếng Anh), language identification (nhận dạng ngôn ngữ).
- Độ chính xác: Theo tài liệu của OpenAI, Whisper đạt độ chính xác cao và ổn định trên nhiều ngôn ngữ, đặc biệt trong điều kiện nhiễu.

#### b) Web Speech API
API tích hợp sẵn trong trình duyệt (Chrome, Edge) hỗ trợ STT real-time, không cần server. Hạn chế: chỉ hoạt động khi có kết nối internet, độ chính xác phụ thuộc vào engine của trình duyệt.

Trong đề tài, Web Speech API được sử dụng cho ghi âm real-time, Whisper làm fallback cho các trường hợp cần xử lý audio chất lượng cao (tối đa 25MB).

### 2.1.4. Text Embedding và RAG

#### a) Text Embedding
Text embedding là kỹ thuật biểu diễn văn bản dưới dạng vector số (dense vector) trong không gian đa chiều, giúp đo lường độ tương đồng (similarity) giữa các văn bản. Các phương pháp phổ biến:
- Word2Vec, GloVe: Embedding mức từ (word-level).
- BERT embeddings: Contextualized embeddings (embedding phụ thuộc ngữ cảnh).
- OpenAI embeddings: Các mô hình như text-embedding-ada-002 (1536 dimensions) được sử dụng cho similarity search.

#### b) Retrieval-Augmented Generation (RAG)
RAG là kỹ thuật kết hợp retrieval (tìm kiếm thông tin) và generation (sinh văn bản):
1. Retrieval: Tìm tài liệu liên quan từ knowledge base dựa trên query embedding.
2. Augmentation: Bổ sung context từ tài liệu tìm được vào prompt.
3. Generation: LLM sinh câu trả lời dựa trên context được augment.

Ứng dụng: Hỏi đáp trên tài liệu dài (>10,000 tokens), chatbot doanh nghiệp với knowledge base riêng, giảm hallucination (ảo giác) của LLMs.

Lưu ý: Đề tài hiện tại chưa triển khai RAG đầy đủ (không sử dụng vector database như FAISS, Pinecone). Phương pháp hiện tại là truncate document và gửi trực tiếp cho AI. RAG được xác định là hướng phát triển trong Chương 5.

### 2.1.5. Nguyên tắc thiết kế giao diện người dùng cho chatbot

a) Usability (Khả năng sử dụng)
- Clarity (Rõ ràng): Giao diện trực quan, dễ hiểu. Phân biệt rõ message của user và AI bằng màu sắc, vị trí và avatar.
- Efficiency (Hiệu quả): Giảm thiểu số thao tác cần thiết. Ví dụ: 6 nút chức năng cho phép truy cập nhanh các chế độ xử lý.
- Feedback (Phản hồi): Hệ thống phản hồi real-time. Typing indicator khi AI đang xử lý, toast notification cho thông báo thành công/lỗi.
- Error Prevention (Ngăn ngừa lỗi): Validate input trước khi xử lý. Ví dụ: Kiểm tra file type và size trước khi upload.

b) User Experience (UX)
- Conversational Flow: Giao diện giống cuộc trò chuyện tự nhiên với message bubbles theo thứ tự thời gian.
- Consistency (Nhất quán): Màu sắc, icon (FontAwesome), terminology thống nhất trong toàn bộ ứng dụng.
- Accessibility (Khả năng tiếp cận): Hỗ trợ người khuyết tật thông qua STT (cho người khó đánh máy), keyboard shortcuts, color contrast cao (WCAG 2.1), và khả năng tương thích với screen reader.
- Responsiveness: Tương thích đa thiết bị (desktop, tablet, mobile) với breakpoint 768px.

c) Best Practices từ ChatGPT
- Dark theme: Giảm mỏi mắt, tạo cảm giác chuyên nghiệp.
- Sidebar lịch sử: Dễ dàng quay lại các cuộc trò chuyện trước đó.
- Auto-scroll: Tự động scroll xuống tin nhắn mới nhất.
- Copy button: Sao chép câu trả lời AI nhanh chóng.
- Settings modal: Cho phép tùy chỉnh trải nghiệm cá nhân (AI provider, ngôn ngữ, theme).

Đề tài áp dụng thiết kế ChatGPT-style với các nguyên tắc usability và UX nêu trên, đảm bảo trải nghiệm người dùng tốt và dễ tiếp cận.

---

Phần tiếp theo (2.2) sẽ trình bày chi tiết các công nghệ: Django, HTML/CSS/JavaScript, Web Speech API, PyPDF2, python-docx, localStorage.
