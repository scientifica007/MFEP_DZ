# Task: discover-legal-text

## الهدف

العثور على المرجع الرسمي لنص قانوني/تنظيمي/إداري مرشح وتثبيت هويته دون ادعاء أكثر مما يثبته المصدر.

## Input

واحد أو أكثر من:

```yaml
query:
  title_fragment: null
  legal_form: null
  number: null
  year: null
  date: null
  ministry_or_sector: null
  keywords_ar: []
  keywords_fr: []
```

## Required process

1. ابدأ بالمصادر الرسمية حسب `ai/context/source-policy.json`.
2. استعمل JORADP/SCALER عند توفره لتثبيت طبيعة النص ورقمه وتاريخه والجريدة.
3. حل رابط العربية الرسمي.
4. حل رابط الفرنسية عند توفرها.
5. قارن البيانات المرجعية بين نتائج البحث وملف الجريدة.
6. إذا كان هناك أكثر من مرشح، لا تدمجهم؛ أعد قائمة مرشحين مع أسباب التمييز.
7. لا تحدد الحالة القانونية في هذه المهمة إلا إذا كانت مطلوبة صراحة وكانت الأدلة كافية.

## Output

```yaml
candidates:
  - identity:
      legal_form: null
      number: null
      date: null
      title_ar: null
      title_fr: null
    publication:
      journal_number: null
      publication_date: null
      pages: null
    sources:
      ar: null
      fr: null
      scaler_or_index: null
    verification:
      identity_confirmed: false
      notes: []
```

## Failure behavior

- إذا تعذر العثور على المصدر الرسمي: `identity_confirmed: false`.
- إذا كانت الذاكرة العامة للنموذج تعرف النص لكن المصدر غير متاح، لا تحول الذاكرة إلى evidence.
- سجل عبارات البحث التي نجحت أو فشلت إذا كانت مفيدة لإعادة التنفيذ.
