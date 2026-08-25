# Task: extract-relations

## الهدف

استخراج العلاقات القانونية بين النصوص أو المواد مع التمييز بين الإحالة العامة والأثر القانوني المباشر.

## Input

```yaml
source_text_id: null
source_material:
  visas: []
  articles: []
  publication_source: null
```

## Required process

1. افحص التأشيرات والمواد والأحكام الختامية منفصلة.
2. أنشئ `references` فقط عندما لا يوجد دليل كاف لعلاقة أدق.
3. لا تصنف `amends`, `supplements`, `repeals`, `partially_repeals`, `replaces` إلا مع صياغة أو أثر صريح يمكن إسناده إلى موضع.
4. ميز `legal_basis` عن `enabling_legislation` وعن `implements`.
5. اربط المادة المصدر بالمادة الهدف متى حددها النص.
6. سجل النص الخام الدال أو موضعه دون اقتباس زائد غير ضروري.
7. لا تدخل العلاقة العكسية يدويا إذا كان النظام يستطيع اشتقاقها.

## Output

```yaml
relations:
  - type: references
    source: null
    target: null
    target_article: null
    evidence:
      source_article: null
      source_page: null
      source_url: null
      evidence_kind: null
    verification:
      stage: machine_extracted
      confidence: null
```

## High-impact relations

تحتاج evidence صريحا قبل قبولها:

- `amends`
- `supplements`
- `repeals`
- `partially_repeals`
- `replaces`
- `derogates_from`

## Validation failures

- target غير محدد مع الادعاء بعلاقة عالية الأثر.
- evidence فارغ في تعديل/إلغاء.
- تحويل كل «وبمقتضى» إلى `implements`.
- استنتاج علاقة من تشابه عنوانين فقط.
