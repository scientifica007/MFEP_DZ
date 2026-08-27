# MFEP_DZ

قاعدة معرفة قانونية مفتوحة ومهيكلة للنصوص التشريعية والتنظيمية والإدارية المرتبطة بقطاع التكوين والتعليم المهنيين في الجزائر.

الهدف هو بناء **ذاكرة قانونية قابلة للقراءة البشرية والاستدعاء الآلي** تسمح بتحديد هوية النص، مصدره، مرتبته ووظيفته القانونية، مواده، علاقاته بالنصوص الأخرى، وحالته القانونية في تاريخ معين مع provenance واضح.

## مبادئ المشروع

1. **المصدر الرسمي أولا:** JORADP والأمانة العامة للحكومة هما المرجع الأول للنصوص المنشورة.
2. **النص القانوني هو وحدة المعرفة**؛ ملف PDF وعدد الجريدة مصدران لا الكيان المركزي.
3. **لا PDF داخل Git:** تحفظ الروابط والمحددات الرسمية فقط، بينما يخزن المشروع Markdown/JSONL/YAML ونصوصا خفيفة قابلة للفهرسة والمراجعة. راجع [`docs/STORAGE_POLICY.md`](docs/STORAGE_POLICY.md).
4. **Human + Machine:** لكل نص `README.md` للإنسان، و`record.yml` و`articles.jsonl` للآلة، مع transcription وحالة تحقق صريحة.
5. **النظام القانوني شبكة متعددة الأبعاد:** نفصل بين المرتبة القانونية، شكل النص، الجهة المختصة، الوظيفة، النطاق والعلاقات.
6. **العربية والفرنسية مساران متقابلان للتحقق:** نرجع إلى الفرنسية الرسمية عند فساد استخراج العربية ثم نتحقق من العربية بصريا في المواضع الحرجة.
7. **لا حالة قانونية بلا تاريخ ودليل:** لا نستنتج `active` أو `repealed` من العمر أو الاسم.
8. **العلاقات القانونية قابلة للتدقيق:** `implements`, `amends`, `repeals`, `provides_for_implementing_act` وغيرها تحفظ مع موضع الدليل حيث أمكن.
9. **الأصل والتعديل والنسخة الموحدة طبقات منفصلة:** لا يدمج تعديل لاحق صامتا في transcription الأصلية.
10. **المشروع Model-Agnostic وProvider-Agnostic:** الحقيقة القانونية لا تعتمد على نموذج ذكاء اصطناعي بعينه.
11. **فشل رابط JORADP لا يعني فقدان المصدر:** هوية العدد هي السنة + الرقم + اللغة؛ يحفظ الرابط المسجل وتستخدم طبقة resolver للعثور على endpoint عامل.
12. **فهرس JORADP أداة اكتشاف لا إثبات نهائي:** وسوم `نص تطبيقي` و`معدل` و`ملغى` تولد مرشحات، ثم تثبت العلاقة من النص المنشور.
13. **سلامة المستودع تتحقق آليا:** GitHub Actions يشغل Validator حتميا بعد كل push إلى `main`.

## القراءة البشرية

- [فهرس corpus البشري](corpus/INDEX.md)
- [عقد حزم النصوص](corpus/texts/README.md)

يوجد حاليا **19 سجلا قانونيا** في دورة staging/validation، وكلها تحت `corpus/texts/`.

البنية المعتادة:

```text
corpus/texts/<TEXT_ID>/
├── README.md
├── record.yml
├── VERIFICATION.md
├── text/
│   ├── ar.md
│   └── fr.md
├── data/
│   └── articles.jsonl
└── sources/
    └── sources.yml
```

وقد تضاف ملفات مثل `amendment-index.jsonl`, `transitional-effects.jsonl`, `forward-search.yml` أو طبقة `consolidated/<DATE>/` بحسب طبيعة النص.

> وجود الحزمة لا يعني أن المتن الكامل متحقق. يجب دائما قراءة حالة اللغة في `text/ar.md`, `text/fr.md` وحقول `verification`.

## Corpus الحالي وفهارسه

- Seed الأساسي:
  - [`metadata/staging/seed-001.jsonl`](metadata/staging/seed-001.jsonl)
  - [`metadata/staging/seed-002-dependencies.jsonl`](metadata/staging/seed-002-dependencies.jsonl)
- التوسع الموضوعي الحديث:
  - [`metadata/staging/sector-expansion.jsonl`](metadata/staging/sector-expansion.jsonl)
- سلسلة التكوين المهني في المؤسسة 1982–1986:
  - [`metadata/staging/historical-enterprise-training.jsonl`](metadata/staging/historical-enterprise-training.jsonl)
- سلسلة CFPA التاريخية:
  - [`metadata/staging/historical-cfpa.jsonl`](metadata/staging/historical-cfpa.jsonl)
- قائمة الاكتشاف:
  - [`metadata/discovery-queue.jsonl`](metadata/discovery-queue.jsonl)

حواف Graph موزعة بالتوازي تحت `graph/staging/`، ومنها:

- [`seed-001-relations.jsonl`](graph/staging/seed-001-relations.jsonl)
- [`seed-002-relations.jsonl`](graph/staging/seed-002-relations.jsonl)
- [`sector-expansion-relations.jsonl`](graph/staging/sector-expansion-relations.jsonl)
- [`historical-enterprise-training-relations.jsonl`](graph/staging/historical-enterprise-training-relations.jsonl)
- [`historical-cfpa-relations.jsonl`](graph/staging/historical-cfpa-relations.jsonl)

## سلاسل قانونية ممثلة حاليا

### المؤسسات الخاصة للتكوين أو التعليم المهني

`18-162 → 20-340 → نسخة بحثية موحدة بتاريخ قطع 2020-12-02`

- الأصل AR/FR متحقق.
- التعديل 20-340 مفهرس على مستوى المواد.
- النسخة الموحدة بحثية وليست نصا رسميا مستقلا.

### التكوين المهني المتواصل

`قانون 08-07 المادة 20 → 24-74`

- 24-74 يطبق المادة 20.
- ألغى نظام التكوين المهني في المؤسسة لسنة 1982.
- قراراته التطبيقية للمواد 13 و14 و22 ما تزال `unresolved` بعد البحث المنجز.

### التكوين المهني في المؤسسة

`82-298 / 82-299 / 82-300 → تعديل 82-300 بواسطة 86-241 → الإلغاء بواسطة 24-74 في 2024`

### مراكز التكوين المهني والتمهين CFPA

`92-27 → تعديل المادة 27 بواسطة 96-99 → الإلغاء بواسطة 14-140 في 2014`

- 14-140 يحافظ انتقاليا على الملحقات المنشأة بموجب المادة 3 من 92-27 إلى غاية حلها أو تحويلها إلى مراكز.
- كما يحافظ على النصوص التطبيقية لـ92-27 إلى غاية صدور النصوص التطبيقية الجديدة.

## المصادر والروابط

- [`docs/SOURCES.md`](docs/SOURCES.md)
- [`docs/JORADP_URL_RESOLUTION.md`](docs/JORADP_URL_RESOLUTION.md)
- [`docs/JORADP_INDEX_DISCOVERY.md`](docs/JORADP_INDEX_DISCOVERY.md)

كل صفحة بشرية تعرض رابط PDF الرسمي عندما يكون endpoint محسومًا. إذا لم يحسم الرابط، يذكر ذلك صراحة ولا ينشأ رابط تخميني.

## النسخ الموحدة

راجع [`docs/AMENDMENTS_AND_CONSOLIDATION.md`](docs/AMENDMENTS_AND_CONSOLIDATION.md).

أول نسخة بحثية موحدة:

[`DZ-DE-2018-162@consolidated-2020-12-02`](corpus/texts/DZ-DE-2018-162/consolidated/2020-12-02/README.md)

النسخة الموحدة تحمل تاريخ قطع، provenance لكل مادة، ولا تقدم بوصفها نصا رسميا مستقلا.

## CI والتحقق

Workflow:

`.github/workflows/validate-repository.yml`

يشغل:

```bash
python scripts/test_joradp_resolver.py
python scripts/validate_repository.py .
```

راجع [`docs/CI.md`](docs/CI.md).

في آخر تحقق بعد إدخال سلسلة CFPA التاريخية سجل الـValidator:

```text
metadata_records: 19
human_readmes: 19
graph_edges: 46
discovery_queue: 29
eval_cases: 17
eval_expected: 17
pdf_files: 0
OK: no deterministic validation errors found.
```

نجاح CI يعني سلامة القواعد الحتمية المعرفة حاليا، ولا يعني تلقائيا أن كل transcription أو كل حالة قانونية أصبحت موثقة بالكامل.

## منهجية وذاكرة المشروع

- [`PROJECT_MEMORY.md`](PROJECT_MEMORY.md)
- [`KNOWLEDGE_CHANGELOG.md`](KNOWLEDGE_CHANGELOG.md)
- [`docs/LEGAL_SYSTEM_DZ.md`](docs/LEGAL_SYSTEM_DZ.md)
- [`docs/METHODOLOGY.md`](docs/METHODOLOGY.md)
- [`docs/LANGUAGE_POLICY.md`](docs/LANGUAGE_POLICY.md)
- [`docs/HUMAN_MACHINE_CORPUS.md`](docs/HUMAN_MACHINE_CORPUS.md)
- [`docs/DATA_MODEL.md`](docs/DATA_MODEL.md)
- [`docs/LEGAL_RELATIONS.md`](docs/LEGAL_RELATIONS.md)
- [`docs/TAXONOMY.md`](docs/TAXONOMY.md)
- [`docs/DECISIONS.md`](docs/DECISIONS.md)
- [`ontology/core.yml`](ontology/core.yml)
- [`AGENTS.md`](AGENTS.md)
- [`ai/HANDOFF.md`](ai/HANDOFF.md)

## مراقبة الجديد في JORADP

اقتراح المراجعة الأسبوعية العامة موثق في [`docs/UPDATE_MONITORING.md`](docs/UPDATE_MONITORING.md) وحالته حاليا `proposal_not_activated`. لم تُنشأ مهمة مجدولة بعد.
