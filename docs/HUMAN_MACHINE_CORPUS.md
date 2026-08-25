# نموذج Human + Machine للنص القانوني

## الهدف

يجب أن يستطيع الإنسان والآلة الوصول إلى **نفس الكيان القانوني** دون إنشاء قاعدتي حقيقة منفصلتين.

## الحزمة الدائمة

```text
corpus/texts/<TEXT_ID>/
├── README.md
├── record.yml
├── text/
│   ├── ar.md
│   └── fr.md
├── data/
│   └── articles.jsonl
└── sources/
    └── sources.yml
```

## `README.md` — الإنسان

يجيب بسرعة عن:

- ما النص؟
- ما رقمه وتاريخه؟
- أين نشر؟
- ما حالته القانونية؟
- ما موضوعه؟
- ما خريطة مواده؟
- ما أهم النصوص المرتبطة به؟
- أين النسخة العربية والفرنسية؟
- ما مستوى التحقق؟

الشرح والفهرسة في README من عمل المشروع، ولا يخلطان بالنص الرسمي.

## `record.yml` — سجل الكيان

يحمل الهوية، النشر، التصنيف القانوني، الجهات، الحالة، اللغات، روابط المحتوى، provenance وverification.

## `articles.jsonl` — الاستدعاء الدقيق

لكل مادة معرف ثابت:

```text
<TEXT_ID>#art-<N>
```

في المرحلة الأولى يمكن أن يحتوي السجل على locator وموضوع وحالة transcription. بعد اعتماد transcription يمكن إضافة payload النصي للمادة أو مرجع مباشر إلى segment داخل ملف اللغة.

## `text/ar.md` و`text/fr.md`

هذه ملفات نصية وليست PDF. تمر حالتها على الأقل عبر:

- `transcription_pending`
- `transcribed`
- `verified`

لا يجوز للـAI أو الواجهة البشرية تقديم transcription غير متحققة على أنها المتن الرسمي الموثوق.

## `sources.yml`

يحفظ المصدر الرسمي دون binary:

- URL؛
- اللغة والدور؛
- رقم الجريدة؛
- تاريخ النشر؛
- page locators؛
- تاريخ الاسترجاع؛
- ملاحظات التحقق.

## مسار البيانات

```text
JORADP external PDF
       ↓ temporary fetch only
text extraction
       ↓
quality check
       ↓
AR/FR alignment
       ↓
transcription review
       ↓
article segmentation
       ↓
record + articles + graph
       ↓
README human view
```

لا يبقى PDF بعد مرحلة الاستخراج.

## قاعدة عدم الازدواج

عند نقل سجل من `corpus/staging/` إلى `corpus/texts/`:

1. تنشأ الحزمة الدائمة؛
2. يحدث `metadata/*.jsonl` إلى `record.yml` الجديد؛
3. يتحقق من المسارات؛
4. تحذف نسخة record القديمة؛
5. يبقى تاريخ Git هو سجل الهجرة.

## الاستدعاء بالذكاء الاصطناعي

عندما يطلب المستخدم مادة بعينها، يكون ترتيب الاستدعاء:

1. resolve `TEXT_ID`؛
2. resolve `#art-N` من `articles.jsonl`؛
3. افحص `text_status`؛
4. إن كان `verified` استخدم النص الداخلي؛
5. إن لم يكن، لا تدّع وجود متن داخلي موثوق، واستعمل المصدر الرسمي وفق سياسة المشروع.

## أول تطبيق

`corpus/texts/DZ-LAW-2008-007/` هو أول تطبيق فعلي للنموذج. يجب استخدام المشكلات التي تظهر أثناء إكمال transcription فيه لتحسين Schema قبل تعميم النموذج على بقية corpus.
