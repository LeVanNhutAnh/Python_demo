# BẢNG PHÂN CÔNG CÔNG VIỆC NHÓM 01
## ĐỀ TÀI: SPEECH TO TEXT AI ASSISTANT - CHUYỂN ĐỔI GIỌNG NÓI THÀNH VĂN BẢN VÀ TƯƠNG TÁC VỚI AI THÔNG MINH

**Môn học:** Lập trình Python  
**Lớp:** DH22TIN06  
**Giảng viên hướng dẫn:** Đặng Mạnh Huy  
**Thời gian thực hiện:** 6 tuần (Tháng 10/2025)

---

## THÀNH VIÊN NHÓM

| STT | Họ và tên | MSSV | Vai trò |
|-----|-----------|------|---------|
| 1 | Lê Văn Nhựt Anh | 221222 | **Nhóm trưởng** - Backend Developer |
| 2 | Nguyễn Văn Ngoan | 226400 | Frontend Developer & UI/UX Designer |
| 3 | Đặng Cảnh Anh Hào | 221250 | AI Integration & API Developer |
| 4 | Nguyễn Trọng Nghĩa | 221122 | Testing & Documentation |

---

## PHÂN CÔNG CHI TIẾT THEO GIAI ĐOẠN

### 📌 GIAI ĐOẠN 1: NGHIÊN CỨU VÀ THIẾT KẾ (Tuần 1-2)

#### **Lê Văn Nhựt Anh** (Nhóm trưởng - Backend)
- ✅ Quản lý tiến độ chung của nhóm
- ✅ Thiết kế kiến trúc hệ thống 3 tầng (Client-Server-AI)
- ✅ Thiết kế database schema (SQLite3):
  - Bảng Conversation, Message, Document, Settings
- ✅ Thiết kế API endpoints:
  - `/ai-chat/`
  - `/analyze-document/`
  - `/whisper-transcribe/`
- ✅ Cấu hình môi trường Django
- ✅ Nghiên cứu cơ chế fallback 3 tầng

**Thời gian:** 14 ngày  
**Deliverables:** 
- Sơ đồ kiến trúc hệ thống
- Database schema
- API documentation draft

---

#### **Nguyễn Văn Ngoan** (Frontend & UI/UX)
- ✅ Nghiên cứu giao diện ChatGPT
- ✅ Thiết kế wireframe và mockup:
  - Sidebar lịch sử
  - Main chat area
  - Input area với 6 nút chức năng
  - Modal settings và history
- ✅ Thiết kế color scheme (Dark theme: #0f1724)
- ✅ Thiết kế responsive breakpoint (768px)
- ✅ Tạo prototype trên Figma/Adobe XD
- ✅ Nghiên cứu HTML5, CSS3, JavaScript ES6+

**Thời gian:** 14 ngày  
**Deliverables:**
- Wireframe/Mockup hoàn chỉnh
- Style guide (màu sắc, font chữ, icon)
- Prototype tương tác

---

#### **Đặng Cảnh Anh Hào** (AI Integration)
- ✅ Nghiên cứu OpenAI API:
  - GPT-3.5 Turbo
  - Whisper API
- ✅ Nghiên cứu Google Gemini API
- ✅ Đăng ký và test API keys
- ✅ Nghiên cứu PyPDF2 và python-docx
- ✅ Thiết kế prompt templates cho 5 chế độ:
  - Hỏi đáp
  - Dịch thuật
  - Tóm tắt
  - Cải thiện văn bản
  - Sửa dấu câu
- ✅ Nghiên cứu Web Speech API

**Thời gian:** 14 ngày  
**Deliverables:**
- Tài liệu tổng hợp API
- Prompt templates
- Demo code kết nối API

---

#### **Nguyễn Trọng Nghĩa** (Testing & Documentation)
- ✅ Viết Chương 1: Giới thiệu
  - Bối cảnh nghiên cứu
  - Mục tiêu
  - Phạm vi
- ✅ Viết Chương 2: Nghiên cứu (phần lý thuyết)
  - NLP, LLMs, Transformer
  - Speech-to-Text
  - RAG
- ✅ Thiết kế test cases:
  - Unit tests
  - Integration tests
  - User acceptance tests
- ✅ Chuẩn bị môi trường test

**Thời gian:** 14 ngày  
**Deliverables:**
- Chương 1 & 2 báo cáo (15-20 trang)
- Bảng test cases chi tiết
- Test plan document

---

### 📌 GIAI ĐOẠN 2: PHÁT TRIỂN (Tuần 3-5)

#### **Lê Văn Nhựt Anh** (Backend Developer)
**Nhiệm vụ chính:**
- ✅ Xây dựng file `views.py` (~385 dòng):
  - `ai_chat()` - Xử lý hội thoại
  - `analyze_document()` - Phân tích tài liệu
  - `whisper_transcribe()` - Chuyển giọng nói
- ✅ Triển khai cơ chế fallback 3 tầng:
  ```python
  try: GPT-3.5
  except: try Gemini
  except: Demo response
  ```
- ✅ Viết hàm hỗ trợ:
  - `extract_text_from_pdf()`
  - `extract_text_from_docx()`
  - `generate_smart_demo_response()`
  - `auto_add_punctuation()`
- ✅ Cấu hình CSRF protection
- ✅ Xử lý file upload (max 10MB/25MB)
- ✅ Xử lý timeout và error handling
- ✅ Token limiting (500/800/300 tokens)

**Chi tiết code:**
- Dòng 342-365: Fallback mechanism
- Dòng 141-170: Document analysis
- Dòng 231-312: Whisper API handling

**Thời gian:** 21 ngày  
**Deliverables:**
- views.py hoàn chỉnh (385 dòng)
- Backend APIs hoạt động ổn định
- Postman/Thunder Client test collection

---

#### **Nguyễn Văn Ngoan** (Frontend Developer)
**Nhiệm vụ chính:**
- ✅ Xây dựng `home.html` (~1900 dòng):
  - HTML structure
  - CSS styling (dark theme)
  - JavaScript class `AIAssistant`

**HTML/CSS (Dòng 1-800):**
- ✅ Sidebar với lịch sử chat
- ✅ Main chat area với typing indicator
- ✅ 6 function buttons:
  - 💬 Hỏi đáp | 🌐 Dịch | 📄 Tóm tắt
  - ✏️ Cải thiện | ✓ Sửa dấu | 📁 Tải file
- ✅ Input area với mic button
- ✅ Modal settings & history
- ✅ Toast notifications
- ✅ Badge display (AI provider, document info)
- ✅ Responsive CSS (breakpoint 768px)

**JavaScript (Dòng 800-1900):**
- ✅ Class `AIAssistant` (OOP):
  - `constructor()` - Khởi tạo
  - `sendMessage()` - Gửi tin nhắn
  - `handleFileUpload()` - Upload file
  - `toggleRecording()` - Ghi âm
  - `addMessage()` - Hiển thị tin nhắn
  - `saveToHistory()` - Lưu localStorage
  - `loadHistory()` - Tải lịch sử
- ✅ Tích hợp Web Speech API
- ✅ localStorage management (max 50 chats)
- ✅ Event handlers
- ✅ Animations & transitions
- ✅ Hàm `removeMarkdownSyntax()` (dòng 1810-1862)

**Thời gian:** 21 ngày  
**Deliverables:**
- home.html hoàn chỉnh (1900+ dòng)
- Giao diện hoạt động mượt mà
- Demo video tương tác

---

#### **Đặng Cảnh Anh Hào** (AI Integration Specialist)
**Nhiệm vụ chính:**
- ✅ Tích hợp OpenAI GPT-3.5:
  - Setup API key trong `settings.py`
  - Xử lý chat completion
  - Token management
  - Error handling (quota, timeout)
- ✅ Tích hợp Google Gemini:
  - Gemini Flash model
  - Fallback mechanism
  - Free tier optimization
- ✅ Tích hợp Whisper API:
  - Audio file processing
  - Language detection (8 ngôn ngữ)
  - Timeout 30s
  - File cleanup
- ✅ Xử lý tài liệu:
  - PyPDF2 cho PDF
  - python-docx cho DOCX
  - Text extraction & cleaning
  - Language detection
  - Word/page counting
- ✅ Tối ưu prompt engineering:
  - Dịch: "Translate to English: {text}"
  - Tóm tắt: "Summarize in Vietnamese: {text}"
  - Q&A: "Answer based on context: {doc}\nQuestion: {q}"
- ✅ Hàm tự động chấm câu tiếng Việt:
  ```python
  def auto_add_punctuation(text):
      # Regex patterns
      text = re.sub(r'\s+', ' ', text)
      text = re.sub(r'(\w+)\s+(và|hoặc)\s+', r'\1, \2 ', text)
      # ... (23 dòng code)
  ```

**Chi tiết kỹ thuật:**
- GPT-3.5 token limits: 4K context
- Gemini token limits: 32K context
- Whisper: max 25MB audio
- Document: max 10MB file

**Thời gian:** 21 ngày  
**Deliverables:**
- API integration hoàn chỉnh
- Prompt templates tối ưu
- Demo các chức năng AI
- Chi phí API tracking

---

#### **Nguyễn Trọng Nghĩa** (Testing & Documentation)
**Nhiệm vụ chính:**

**Testing (10 ngày):**
- ✅ Kiểm thử chức năng:
  - TC-01: Chat cơ bản
  - TC-02: Dịch thuật
  - TC-03: Upload PDF
  - TC-04: Speech-to-Text
  - TC-05: Q&A theo file
  - TC-06: File quá lớn (error handling)
  - TC-07: Fallback mechanism
- ✅ Kiểm thử hiệu năng (500 requests):
  - Đo latency
  - Phân tích phân bố thời gian
  - Stress testing
- ✅ Khảo sát người dùng (20 users):
  - Mức độ hài lòng (4.3/5)
  - SUS Score (82.5/100)
  - Phản hồi định tính
- ✅ Thu thập metrics:
  - ROUGE-L: 0.64
  - STT accuracy: 92%
  - Upload success: 96.5%

**Documentation (11 ngày):**
- ✅ Viết Chương 3: Phân tích và thiết kế
  - Yêu cầu hệ thống
  - Kiến trúc hệ thống
  - Thiết kế database
  - Thiết kế UI/UX
  - Thiết kế API
- ✅ Viết Chương 4: Triển khai
  - Môi trường phát triển
  - Quy trình xử lý
  - Thử nghiệm
  - Đánh giá chất lượng
  - Các vấn đề kỹ thuật
- ✅ Chụp screenshots demo
- ✅ Ghi chú code (comments)
- ✅ Viết file `README.md`

**Thời gian:** 21 ngày  
**Deliverables:**
- Bảng test results (Bảng 4.2, 4.3, 4.4)
- Chương 3 & 4 báo cáo (30-35 trang)
- Screenshots & video demo
- README.md hướng dẫn cài đặt

---

### 📌 GIAI ĐOẠN 3: KIỂM THỬ VÀ HOÀN THIỆN (Tuần 6)

#### **Lê Văn Nhựt Anh** (Backend)
- ✅ Debug và fix bugs backend
- ✅ Tối ưu code:
  - Rút gọn văn bản dài (3000 ký tự)
  - Xóa file tạm tự động
  - Cải thiện error messages
- ✅ Security review:
  - CSRF token
  - File validation
  - API key protection
- ✅ Performance tuning
- ✅ Deploy lên localhost
- ✅ Chuẩn bị demo

**Thời gian:** 7 ngày

---

#### **Nguyễn Văn Ngoan** (Frontend)
- ✅ Debug và fix bugs giao diện
- ✅ Tối ưu UX:
  - Auto-scroll tin nhắn mới
  - Loading indicators
  - Toast notifications
  - Badge updates
- ✅ Cross-browser testing (Chrome, Edge, Safari)
- ✅ Mobile responsive testing
- ✅ Animations polish
- ✅ Accessibility review:
  - Keyboard shortcuts
  - ARIA labels
  - Color contrast (WCAG 2.1 AA)
- ✅ Chuẩn bị video demo UI

**Thời gian:** 7 ngày

---

#### **Đặng Cảnh Anh Hào** (AI Integration)
- ✅ Kiểm tra fallback mechanism
- ✅ Test với nhiều loại input:
  - Văn bản dài
  - Các ngôn ngữ khác nhau
  - File PDF/DOCX khác nhau
  - Audio chất lượng khác nhau
- ✅ Tối ưu chi phí API:
  - Token limiting
  - Caching (nếu có)
  - Rate limiting
- ✅ Đo đạc accuracy:
  - STT: 92%
  - Translation: 88%
  - Summary ROUGE-L: 0.64
- ✅ Tạo demo cases:
  - 7 kịch bản thực tế (4.7)

**Thời gian:** 7 ngày

---

#### **Nguyễn Trọng Nghĩa** (Testing & Doc)
- ✅ Regression testing toàn bộ hệ thống
- ✅ Viết Chương 5: Kết luận và kiến nghị
  - Đánh giá hoàn thành (Bảng 5.1)
  - Đóng góp chính
  - Kết quả đo lường (Bảng 5.2)
  - Kiến nghị ngắn/trung/dài hạn
  - Hạn chế và hướng phát triển
- ✅ Hoàn thiện tài liệu:
  - Phụ lục A: Mã nguồn
  - Phụ lục B: Hướng dẫn cài đặt
  - Phụ lục C: Test cases
  - Danh mục tài liệu tham khảo
- ✅ Format báo cáo hoàn chỉnh:
  - Mục lục
  - Danh sách hình/bảng
  - Từ viết tắt
  - Page numbering
- ✅ Review tổng thể
- ✅ Chuẩn bị slides thuyết trình
- ✅ Chuẩn bị câu hỏi bảo vệ

**Thời gian:** 7 ngày  
**Deliverables:**
- Báo cáo hoàn chỉnh (90+ trang)
- Slides PowerPoint
- Video demo đầy đủ
- Source code + README

---

## PHÂN CÔNG THEO LOẠI CÔNG VIỆC

### 📊 Tổng hợp theo tỷ lệ (%)

| Thành viên | Backend | Frontend | AI/API | Testing | Documentation | Tổng |
|------------|---------|----------|--------|---------|---------------|------|
| Lê Văn Nhựt Anh | **70%** | 5% | 10% | 5% | 10% | 100% |
| Nguyễn Văn Ngoan | 5% | **75%** | 5% | 5% | 10% | 100% |
| Đặng Cảnh Anh Hào | 10% | 5% | **70%** | 10% | 5% | 100% |
| Nguyễn Trọng Nghĩa | 5% | 5% | 5% | **40%** | **45%** | 100% |

---

### 📈 Khối lượng công việc (dòng code & trang báo cáo)

| Thành viên | Code | Báo cáo | Tổng output |
|------------|------|---------|-------------|
| Lê Văn Nhựt Anh | **385 dòng** (views.py) | 10 trang | ~395 |
| Nguyễn Văn Ngoan | **1900 dòng** (home.html) | 10 trang | ~1910 |
| Đặng Cảnh Anh Hào | **300 dòng** (AI utils) | 10 trang | ~310 |
| Nguyễn Trọng Nghĩa | 50 dòng (tests) | **60 trang** | ~110 |

**Tổng:** ~2635 dòng code + 90 trang báo cáo

---

## LỊCH TRÌNH CHI TIẾT (6 TUẦN)

### Tuần 1-2: Nghiên cứu & Thiết kế
```
[Anh    ] ████████████████ Backend design
[Ngoan  ] ████████████████ UI/UX design
[Hào    ] ████████████████ API research
[Nghĩa  ] ████████████████ Chương 1 & 2
```

### Tuần 3-4: Phát triển (Phase 1)
```
[Anh    ] ████████████████ views.py (200 dòng)
[Ngoan  ] ████████████████ home.html HTML/CSS (800 dòng)
[Hào    ] ████████████████ OpenAI integration
[Nghĩa  ] ████████████████ Test cases + Chương 3
```

### Tuần 5: Phát triển (Phase 2)
```
[Anh    ] ████████████████ views.py hoàn thiện (185 dòng)
[Ngoan  ] ████████████████ JavaScript (1100 dòng)
[Hào    ] ████████████████ Gemini + Whisper
[Nghĩa  ] ████████████████ Testing + Chương 4
```

### Tuần 6: Hoàn thiện & Bảo vệ
```
[Anh    ] ████████ Debug + Deploy
[Ngoan  ] ████████ Polish UI
[Hào    ] ████████ AI testing
[Nghĩa  ] ████████████████ Chương 5 + Slides
```

---

## MEETINGS & CHECKPOINTS

### Họp nhóm (2 lần/tuần - Thứ 3 & Thứ 6)
- **Thời gian:** 19:00 - 20:30 (1.5h)
- **Địa điểm:** Online (Google Meet) hoặc Phòng lab
- **Nội dung:**
  - Báo cáo tiến độ
  - Review code/design
  - Giải quyết blocking issues
  - Plan công việc tuần sau

### Milestones & Demos
- **Tuần 2 (14/10):** Demo wireframe + database design
- **Tuần 4 (28/10):** Demo backend API + frontend prototype
- **Tuần 5 (04/11):** Integration demo (end-to-end)
- **Tuần 6 (11/11):** Final demo + báo cáo hoàn chỉnh

### Gặp giảng viên (1 lần/2 tuần)
- Tuần 2: Review thiết kế
- Tuần 4: Review code & progress
- Tuần 6: Final review trước bảo vệ

---

## TIÊU CHÍ ĐÁNH GIÁ CÁ NHÂN

### 1. Chất lượng công việc (40%)
- Code chạy đúng, không lỗi
- UI/UX đẹp, dễ dùng
- Tài liệu đầy đủ, rõ ràng
- Test coverage đạt yêu cầu

### 2. Đúng tiến độ (30%)
- Hoàn thành đúng deadline
- Commit code đều đặn
- Tham gia họp nhóm

### 3. Tinh thần làm việc (20%)
- Hỗ trợ đồng đội
- Chủ động giải quyết vấn đề
- Giao tiếp tốt

### 4. Đóng góp sáng tạo (10%)
- Đề xuất ý tưởng hay
- Tối ưu code/UI
- Research thêm công nghệ mới

---

## CÔNG CỤ & QUESN TRỊ DỰ ÁN

### Code Management
- **Git:** GitHub repository
- **Branches:**
  - `main` - Production code
  - `dev` - Development
  - `feature/backend` - Anh
  - `feature/frontend` - Ngoan
  - `feature/ai` - Hào
  - `feature/docs` - Nghĩa

### Task Management
- **Trello Board:** 4 columns
  - To Do
  - In Progress
  - Review
  - Done
- **Mỗi thành viên:** Tự assign tasks, update daily

### Communication
- **Group Zalo:** Hỏi đáp nhanh
- **Email:** Gửi tài liệu chính thức
- **Google Drive:** Chia sẻ tài liệu

### Documentation
- **Google Docs:** Viết báo cáo chung
- **Markdown:** README, API docs
- **Notion:** Knowledge base (optional)

---

## BACKUP PLAN

### Nếu thành viên vắng mặt
- **Anh vắng:** Hào backup backend
- **Ngoan vắng:** Nghĩa backup frontend cơ bản
- **Hào vắng:** Anh backup AI integration
- **Nghĩa vắng:** Ngoan backup documentation

### Nếu công nghệ gặp vấn đề
- **OpenAI quota hết:** Chuyển Gemini 100%
- **Web Speech API lỗi:** Dùng Whisper API
- **Deploy khó:** Demo trên localhost

---

## CAM KẾT CỦA NHÓM

Chúng em, các thành viên nhóm 01, cam kết:

✅ Hoàn thành đầy đủ các nhiệm vụ được phân công  
✅ Tuân thủ thời gian và chất lượng  
✅ Hỗ trợ lẫn nhau trong quá trình thực hiện  
✅ Trung thực trong công việc, không sao chép code  
✅ Tôn trọng ý kiến của giảng viên và đồng đội  

---

**Ngày lập:** 30/10/2025  
**Được phê duyệt bởi:** Giảng viên Đặng Mạnh Huy

---

## CHỮ KÝ XÁC NHẬN

| Họ tên | Chữ ký | Ngày |
|--------|--------|------|
| Lê Văn Nhựt Anh (Nhóm trưởng) | ___________ | ______ |
| Nguyễn Văn Ngoan | ___________ | ______ |
| Đặng Cảnh Anh Hào | ___________ | ______ |
| Nguyễn Trọng Nghĩa | ___________ | ______ |

---

## PHỤ LỤC: CHECKLIST CHO TỪNG THÀNH VIÊN

### ✅ Lê Văn Nhựt Anh - Backend Checklist
- [ ] Cấu hình Django project
- [ ] Tạo 3 endpoints (`/ai-chat/`, `/analyze-document/`, `/whisper-transcribe/`)
- [ ] Viết hàm fallback 3 tầng
- [ ] Viết `extract_text_from_pdf()`
- [ ] Viết `extract_text_from_docx()`
- [ ] Viết `generate_smart_demo_response()`
- [ ] Viết `auto_add_punctuation()`
- [ ] CSRF protection
- [ ] File validation
- [ ] Error handling
- [ ] Timeout handling
- [ ] Token limiting
- [ ] Test với Postman
- [ ] Deploy localhost
- [ ] Code comments đầy đủ

### ✅ Nguyễn Văn Ngoan - Frontend Checklist
- [ ] HTML structure hoàn chỉnh
- [ ] CSS dark theme (#0f1724)
- [ ] Responsive breakpoint 768px
- [ ] Sidebar lịch sử
- [ ] Main chat area
- [ ] 6 function buttons
- [ ] Input area + mic button
- [ ] Modal settings
- [ ] Modal history
- [ ] Toast notifications
- [ ] Badge display
- [ ] Class `AIAssistant`
- [ ] Method `sendMessage()`
- [ ] Method `handleFileUpload()`
- [ ] Method `toggleRecording()`
- [ ] Method `addMessage()`
- [ ] Method `saveToHistory()`
- [ ] Method `loadHistory()`
- [ ] Method `removeMarkdownSyntax()`
- [ ] localStorage management
- [ ] Web Speech API integration
- [ ] Animations & transitions
- [ ] Accessibility (ARIA, keyboard)
- [ ] Cross-browser testing
- [ ] Video demo UI

### ✅ Đặng Cảnh Anh Hào - AI Integration Checklist
- [ ] Đăng ký OpenAI API key
- [ ] Đăng ký Gemini API key
- [ ] Test GPT-3.5 Turbo
- [ ] Test Gemini Flash
- [ ] Test Whisper API
- [ ] Viết prompt templates (5 chế độ)
- [ ] Tích hợp PyPDF2
- [ ] Tích hợp python-docx
- [ ] Language detection
- [ ] Word/page counting
- [ ] Token management
- [ ] Fallback mechanism
- [ ] Error handling (quota, timeout)
- [ ] File cleanup
- [ ] Auto-punctuation tiếng Việt
- [ ] Test 8 ngôn ngữ STT
- [ ] Đo accuracy (STT 92%, ROUGE-L 0.64)
- [ ] Tối ưu chi phí API
- [ ] Demo 7 kịch bản thực tế

### ✅ Nguyễn Trọng Nghĩa - Testing & Documentation Checklist
- [ ] Viết Chương 1: Giới thiệu (10 trang)
- [ ] Viết Chương 2: Nghiên cứu (15 trang)
- [ ] Viết Chương 3: Phân tích & Thiết kế (20 trang)
- [ ] Viết Chương 4: Triển khai (25 trang)
- [ ] Viết Chương 5: Kết luận (15 trang)
- [ ] Phụ lục A: Mã nguồn
- [ ] Phụ lục B: Hướng dẫn cài đặt
- [ ] Phụ lục C: Test cases
- [ ] Danh mục tài liệu tham khảo
- [ ] Mục lục
- [ ] Danh sách hình/bảng
- [ ] Từ viết tắt
- [ ] Viết 7 test cases chi tiết
- [ ] Chạy 500 requests (performance test)
- [ ] Khảo sát 20 users
- [ ] Thu thập metrics (UX 4.3/5, SUS 82.5)
- [ ] Chụp 20+ screenshots
- [ ] Ghi video demo 5-10 phút
- [ ] Viết README.md
- [ ] Comment code
- [ ] Tạo slides thuyết trình
- [ ] Chuẩn bị câu hỏi bảo vệ

---

**🎯 MỤC TIÊU CHUNG: Đạt điểm ≥ 8.5/10 cho đề tài!**

---

*Tài liệu này được cập nhật lần cuối: 30/10/2025*
