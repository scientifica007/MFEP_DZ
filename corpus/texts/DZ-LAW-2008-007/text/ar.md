---
text_id: DZ-LAW-2008-007
language: ar
role: official_publication_transcription
status: transcription_pending
source_manifest: ../sources/sources.yml
pdf_committed: false
---

# القانون رقم 08-07 — النص العربي

هذا الملف مخصص لنسخة **نصية قابلة للبحث** من النص العربي المنشور رسميا.

## الحالة

المصدر الرسمي والصفحات متحقق منها، وفهرس المواد 1–32 موجود في `../data/articles.jsonl`. لم تعتمد بعد نسخة transcription كاملة مادة بمادة داخل Git، لذلك لا يجوز اعتبار هذا الملف بديلا نصيا مكتملا للجريدة الرسمية.

عند materialization يجب:

1. جلب PDF الرسمي مؤقتا من الرابط المسجل في `../sources/sources.yml`؛
2. استخراج الصفحات 4–7 فقط؛
3. تصحيح تشوهات طبقة النص العربية بالتحقق البصري والمقابلة الفرنسية؛
4. تقسيم النص إلى المواد 1–32؛
5. تحديث `status` إلى `transcribed` ثم `verified` بعد المراجعة؛
6. حذف PDF المؤقت وعدم إضافته إلى Git.

الواجهة البشرية المختصرة موجودة في `../README.md`.
