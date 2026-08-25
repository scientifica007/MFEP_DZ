# نموذج البيانات القانوني

هذه الوثيقة تحدد الشكل المفاهيمي لسجل النص القانوني قبل تحويله إلى JSON Schema نهائي. المقصود أن تكون الحقول مستقرة بما يكفي للبحث الآلي، مع السماح بالتوسع التاريخي والقانوني.

## 1. الكيان الأساسي: LegalText

مثال مختصر:

```yaml
id: DZ-DE-2024-047

identity:
  legal_form: executive_decree
  number: "24-47"
  title:
    ar: "..."
    fr: "..."
  signature_date: 2024-02-08

publication:
  journal_number: 10
  publication_date: 2024-02-11
  locators:
    ar:
      start_page: 5
      end_page: 8
    fr:
      start_page: 5
      end_page: 8
  url_ar: "..."
  url_fr: "..."

legal_classification:
  normative_order: regulatory
  legal_function: implementing_regulation
  normative_character: regulatory
  scope: general

institutions:
  issuing_authorities: []
  initiating_ministry: null
  affected_sectors: [vocational_training]

status:
  value: unknown
  as_of: 2026-08-25
  evidence: []

languages: {}
relations: []
provenance: []
verification: {}
```

## 2. `id`

يجب أن يكون:

- فريدا؛
- مستقرا؛
- غير مرتبط بعنوان قد يتغير في التهجئة؛
- قابلا للاستخدام في URL وGraph وJSONL.

الصيغة النهائية لم تعتمد بعد. الصيغة الحالية اقتراح عمل:

`DZ-{DOMAIN?}-{FORM}-{YEAR}-{NUMBER}`

بعد اختبار Seed Corpus 001، تستعمل السجلات المرقمة مؤقتا صيغة أقصر مثل `DZ-DE-2012-125` و`DZ-LAW-2008-007`، ولا يضاف اسم القطاع داخل المعرف إلى أن نثبت أن ذلك لا يؤدي إلى معرفات مرتبطة بتصنيف قد يتغير. أما الأعمال غير المرقمة فتحتاج استراتيجية منفصلة ما تزال قيد الاختبار.

## 3. الهوية `identity`

```yaml
identity:
  legal_form:
  number:
  title:
    ar:
    fr:
    en:
  short_title:
  signature_date:
  promulgation_date:
```

### ملاحظات

- `number` يخزن كنص String للمحافظة على الصفر والشرطة والصيغ التاريخية.
- `title.en` إن وجد يكون ترجمة مشروع ما لم يثبت أنه رسمي.
- لا نضع `promulgation_date` إلا في الأشكال التي ينطبق عليها المفهوم.
- `number: null` قيمة مشروعة للأعمال الرسمية غير المرقمة، مثل بعض القرارات الوزارية المشتركة؛ لا نخترع لها رقما.

## 4. النشر `publication`

```yaml
publication:
  official_gazette: true
  journal_number:
  journal_year:
  publication_date:
  locators:
    ar:
      start_page:
      end_page:
      locator_source:
    fr:
      start_page:
      end_page:
      locator_source:
  url_ar:
  url_fr:
```

### لماذا `locators` حسب اللغة؟

أثبت Seed Corpus 001 أن ترقيم الصفحات في النسخة العربية والترجمة الفرنسية **ليس بالضرورة متطابقا** حتى داخل العدد نفسه. أمثلة مؤكدة في العينة:

- المرسوم التنفيذي 12-125: يبدأ في الصفحة 9 بالعربية والصفحة 8 بالفرنسية؛
- القانون 18-10: يبدأ في الصفحة 7 في الفهرس العربي والصفحة 6 بالفرنسية؛
- القرار الوزاري المشترك المؤرخ في 24 مارس 2022: الفهرس العربي يحيله إلى الصفحة 28، بينما الترجمة الفرنسية تبدأ في الصفحة 26؛
- القرار الوزاري المشترك المؤرخ في 15 فبراير 2026: يقع في الصفحات 24–25 بالعربية و23–24 بالفرنسية.

لذلك لا يجوز استخدام حقل واحد `pages` بوصفه locator مشتركا. الصفحة جزء من **تجسيد لغوي/طبعة معينة** لا من الهوية المجردة للنص القانوني.

يمكن إضافة `locator_source` عندما يأتي رقم الصفحة من فهرس رسمي أو مرجع رسمي آخر قبل تثبيت رابط PDF المباشر.

النصوص الإدارية غير المنشورة في الجريدة الرسمية تستخدم source type مختلفا ولا تخترع لها بيانات جريدة.

## 5. التصنيف القانوني `legal_classification`

```yaml
legal_classification:
  normative_order:
  legal_form:
  legal_function:
  normative_character:
  scope:
  constitutional_or_legal_domain:
```

### قيم أولية لـ`normative_order`

- `constitutional`
- `international`
- `legislative`
- `regulatory`
- `administrative`
- `jurisprudential`

### قيم أولية لـ`normative_character`

- `constitutional`
- `legislative`
- `regulatory`
- `individual_administrative_act`
- `internal_administrative`
- `interpretative`
- `guidance`
- `jurisprudential`

### `legal_function`

قائمة مفتوحة controlled vocabulary، مثل:

- `framework_legislation`
- `sector_legislation`
- `implementing_regulation`
- `autonomous_regulation`
- `amending_text`
- `repealing_text`
- `institutional_organization`
- `institution_creation`
- `treaty_ratification`
- `appointment`
- `procedure_regulation`
- `certification_regulation`

## 6. الجهات `institutions`

```yaml
institutions:
  issuing_authorities:
    - institution_id: ...
      label_as_published:
        ar: "..."
        fr: "..."
  initiating_ministry:
  affected_sectors: []
```

`label_as_published` يحفظ الاسم التاريخي كما ورد ولا يستبدل باسم حديث.

## 7. التواريخ والأثر

```yaml
effect:
  effective_date:
  effective_date_rule:
  expiry_date:
  repeal_date:
  transitional_periods: []
```

`effective_date_rule` يسجل هل التاريخ:

- منصوص عليه صراحة؛
- يبدأ من النشر؛
- مرتبط بنص تطبيقي؛
- مستنتج وفق قاعدة عامة تحتاج توثيقا.

يجب عدم الخلط بين `status.as_of` وبين `effect.repeal_date`: الأول تاريخ تقييم الحالة، أما الثاني فهو تاريخ بدء الأثر القانوني للإلغاء إذا أمكن إثباته.

## 8. الحالة القانونية `status`

```yaml
status:
  value: active|amended|partially_repealed|repealed|expired|suspended|not_yet_effective|unknown
  as_of: YYYY-MM-DD
  confidence: 0.0
  evidence: []
  notes:
```

لا يسمح بحالة غير مؤرخة في النسخة النهائية من Schema.

Seed Corpus 001 أكد ضرورة عدم استعمال `active` لمجرد أن النص حديث أو مستشهد به لاحقا. يمكن أن تثبت الإحالة اللاحقة استمرار الأهمية القانونية، بينما يبقى توصيف الحالة المركبة بحاجة إلى فحص التعديلات والإلغاءات.

## 9. اللغات `languages`

```yaml
languages:
  ar:
    available: true
    role: official_publication
    source_url:
    extraction_method:
    extraction_quality:
    visually_verified:
  fr:
    available: true
    role: official_translation
    source_url:
    extraction_method:
    extraction_quality:
    used_for_recovery:
  en:
    available: false
    role: project_translation
```

يجب أن تبقى بيانات الاستخراج منفصلة حسب اللغة؛ جودة طبقة النص العربية قد تكون منخفضة مع بقاء الصفحة الرسمية صحيحة بصريا، بينما تكون الفرنسية قابلة للاستخراج الآلي بدرجة أعلى.

## 10. البنية الداخلية `structure`

```yaml
structure:
  preamble:
  visas: []
  chapters: []
  articles:
    - id: art-1
      number: "1"
      ar: "..."
      fr: "..."
      alignment_status:
```

يمكن نقل النصوص الطويلة إلى ملفات مستقلة والاكتفاء بالمراجع داخل metadata.

## 11. العلاقات `relations`

```yaml
relations:
  - id: REL-...
    type: implements
    source_ref: DZ-...
    target_ref: DZ-...
    source_article: art-3
    target_article: null
    confidence: 1.0
    evidence:
      language: ar
      page:
      excerpt_or_locator:
```

التفاصيل في `LEGAL_RELATIONS.md`.

العلاقة يمكن أن تشير إلى `target_ref` لم يدخل corpus بعد، بشرط وسمه صراحة في الفهرس أو Graph بأنه unresolved dependency وعدم اختراع metadata له. هذا يسمح بالتوسع عبر Graph Traversal مع بقاء حدود المعرفة واضحة.

## 12. الموضوعات `topics`

```yaml
topics:
  - institutions
  - vocational_training
  - examinations_certification
```

التصنيف متعدد القيم، ويجب أن يعتمد على قاموس controlled vocabulary.

## 13. الكلمات المفتاحية

نفصل بين:

```yaml
keywords:
  official: []
  extracted: []
  curated: []
```

حتى لا نخلط كلمات SCALER/الفهرسة الرسمية مع كلمات مولدة آليا.

## 14. المصدر والأصل `provenance`

```yaml
provenance:
  - source_type: official_gazette
    language:
    url:
    retrieved_at:
    extraction_method:
    parser_version:
    notes:
```

عند غياب رابط مباشر مؤقتا مع وجود إثبات رسمي آخر، يسجل نوع المصدر كما هو، مثل `official_sgg_annual_index`، ولا يوصف بأنه PDF لم يتم الوصول إليه.

## 15. التحقق `verification`

```yaml
verification:
  level: 0
  metadata_verified: false
  source_verified: false
  structure_verified: false
  relations_verified: false
  legal_status_verified: false
  verified_at:
  needs_legal_review: false
```

يمكن استخدام `partial` في ملفات staging خلال فترة تطوير الـSchema، لكن النسخة النهائية ينبغي أن تحدد تمثيلا صارما لهذه الحالة (قيمة تعداد أو حقول تفصيلية).

## 16. فصل الحقائق عن التقييمات

يمكن إضافة:

```yaml
assertions:
  - kind: source_fact|derived_fact|legal_assessment
    value: ...
    evidence: ...
```

خصوصا للحقائق التي لا تنتمي مباشرة إلى حقول Schema الثابتة.

## 17. النصوص الموحدة

```yaml
versions:
  original:
  amendments: []
  consolidated:
    available: false
    as_of:
    generated_by:
    disclaimer:
```

أي consolidated text يجب أن يحمل تاريخا؛ لا توجد «نسخة موحدة» مطلقة خارج الزمن.

## 18. صيغة التخزين

الصيغ المقترحة والمختبرة مبدئيا في Seed Corpus 001:

- YAML/Markdown للملفات الفردية المقروءة بشريا؛
- JSONL لفهرس corpus الكامل؛
- JSONL/JSON/CSV للحواف Graph edges؛
- JSON-LD لاحقا عند استقرار الأنطولوجيا؛
- PDF/raw source references منفصلة؛
- `discovery-queue.jsonl` للتبعيات المكتشفة التي لم تدخل corpus بعد.

## 19. قاعدة التطور

قبل تثبيت JSON Schema نهائي، يجب اختبار النموذج على حالات متنوعة:

1. قانون؛
2. أمر؛
3. مرسوم رئاسي للتصديق على معاهدة؛
4. مرسوم تنفيذي تطبيقي؛
5. قرار وزاري مشترك؛
6. قرار فردي؛
7. تعليمة أو منشور مهم للقطاع؛
8. نص معدل عدة مرات؛
9. نص ملغى جزئيا؛
10. نص قديم بوزارة ذات اسم تاريخي مختلف.

### نتيجة Seed Corpus 001

العينة الأولى غطت بالفعل: قانونا توجيهيا، قانون التمهين، مراسيم تنفيذية تطبيقية ومؤسساتية، نصا تعديليا، نص إنشاء مؤسسات، وقرارين وزاريين مشتركين غير مرقمين بينهما علاقة إلغاء صريحة. وما يزال من الضروري قبل Schema v1 اختبار: الأمر، المرسوم الرئاسي/المعاهدة، القرار الفردي، نص إداري غير منشور، وحالة الإلغاء الجزئي/التعديلات المتعددة المعقدة.
