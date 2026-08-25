# مخرجات الذكاء الاصطناعي

هذا المجلد يصف أو يستضيف، عند الحاجة، مخرجات AI المؤقتة قبل إدخالها إلى corpus أو metadata الموثوقة.

## المبدأ

**AI output ≠ trusted knowledge.**

المخرجات الآلية تمر عبر staging ثم validation ثم promotion وفق متطلبات المهمة.

## حقول تشغيلية مقترحة

```yaml
run:
  provider: null
  model: null
  prompt_version: null
  task_version: null
  timestamp: null

verification:
  stage: machine_extracted
  issues: []
```

هذه الحقول Audit metadata وليست جزءا من هوية النص القانونية.

## قواعد

- لا تحفظ الأسرار أو API keys في المستودع.
- لا تنقل مخرجات نموذج إلى trusted corpus دون provenance وvalidation.
- احتفظ بنتائج الفشل المفيدة للـevals عندما تكشف نمطا منهجيا مهما.
- المخرجات المؤقتة الضخمة يمكن تجاهلها في Git لاحقا؛ أما عقودها وأمثلتها المرجعية فتوثق هنا.