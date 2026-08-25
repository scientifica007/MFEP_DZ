# Task: ingest-legal-text

## الهدف

تحويل نص رسمي مثبت الهوية إلى staging record منظم مع الحفاظ على المصدر الخام وprovenance وعدم خلط الاستخراج بالتفسير.

## Input

```yaml
reference:
  legal_form: null
  number: null
  date: null
  official_sources:
    ar: null
    fr: null
```

## Required process

1. تحقق من الهوية المرجعية قبل الاستخراج.
2. احفظ بيانات المصدر والنسخة واللغة والجريدة والصفحات.
3. استخرج طبقة `raw` دون تصحيح صامت.
4. قيّم جودة العربية.
5. إذا كانت العربية معطوبة، نفذ `align-ar-fr` أو استخدم الفرنسية لاستعادة البنية مع تسجيل ذلك.
6. أنشئ `normalized` للحقول القياسية فقط مع الاحتفاظ بالقيمة الخام.
7. صنف `interpreted` وفق أبعاد النظام القانوني المعتمدة.
8. استخرج التأشيرات والمواد والعلاقات كمرشحين؛ العلاقات عالية الأثر تحتاج evidence.
9. لا تعلن الحالة القانونية الحالية إلا عبر مهمة `determine-status` أو evidence صريح كاف.
10. ضع الناتج في staging لا trusted حتى تحقق شروط الترقية.

## Output contract

```yaml
record:
  id_candidate: null
  identity: {}
  publication: {}
  language_variants: {}
  raw: {}
  normalized: {}
  interpreted: {}
  articles: []
  relations: []
  provenance: []
  verification:
    stage: machine_extracted
    issues: []
```

## Validation

- وجود مصدر رسمي أو تسجيل سبب عدم توفره.
- عدم فقد raw.
- عدم وجود علاقة تعديل/إلغاء بلا evidence.
- عدم وجود `active/repealed` بلا `status_as_of` وevidence.
- تسجيل أي اعتماد على الفرنسية لاستعادة العربية أو البنية.
