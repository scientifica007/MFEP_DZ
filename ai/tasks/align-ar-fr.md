# Task: align-ar-fr

## الهدف

مقابلة النسخة العربية بالفرنسية لحل مشاكل الاستخراج أو البنية أو المصطلحات دون تحويل الفرنسية إلى «نص عربي رسمي».

## Input

```yaml
text_id: null
sources:
  ar: null
  fr: null
focus:
  - metadata
  - structure
  - articles
  - terminology
```

## Required process

1. أثبت أن الوثيقتين تخصان النص القانوني نفسه.
2. قارن العنوان والرقم والتاريخ والجريدة والصفحات.
3. حدد جودة text layer لكل لغة.
4. حاذِ المواد حسب الرقم والبنية لا التشابه الدلالي فقط.
5. عند استعادة قيمة من الفرنسية، سجل أن الفرنسية كانت مصدر الاستعادة.
6. تحقق بصريا من العربية في القيم ذات الأثر القانوني متى كان سبب المقابلة فساد الاستخراج العربي.
7. سجل الفروق الحقيقية ولا تطمسها بترجمة تلقائية.

## Output

```yaml
alignment:
  identity_match: false
  article_pairs: []
  recovered_fields: []
  discrepancies: []
  terminology_notes: []
  verification:
    arabic_visual_check_required: false
    arabic_visual_check_completed: false
```

## Discrepancy types

- `ocr_or_text_layer_error`
- `number_format_difference`
- `terminology_difference`
- `structural_difference`
- `possible_translation_difference`
- `unresolved`

## قاعدة حاسمة

النص الفرنسي يمكن أن يساعد في معرفة ما يجب أن يظهر في العربية، لكنه لا يجيز استبدال النص العربي الخام بترجمة مولدة.