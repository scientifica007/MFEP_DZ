# Scripts — أدوات الحماية والاستخراج

هذه الأدوات لا تعتمد على نموذج ذكاء اصطناعي بعينه. بعضها حواجز deterministic وبعضها أدوات وصول واستخراج من JORADP.

## `joradp_resolver.py`

يحل مشكلة الروابط المباشرة غير المستقرة في JORADP.

المبدأ:

```text
stable source identity = year + issue + language
URL = replaceable access endpoint
```

ترتيب المحاولة:

1. الرابط المسجل في الحزمة؛
2. اختلافات حالة الأحرف وامتداد PDF؛
3. صفحة السنة الرسمية `ZAyyyy` أو `ZFyyyy` واستخراج رابط العدد منها.

مثال:

```bash
python3 scripts/joradp_resolver.py \
  corpus/texts/DZ-DE-2018-162/sources/sources.yml \
  --lang fr \
  --json
```

راجع `docs/JORADP_URL_RESOLUTION.md`.

## `materialize_joradp_text.py`

يستخدم الـresolver أولًا، ثم ينزل PDF العامل إلى مساحة مؤقتة، يشغّل `pdftotext`، ويكتب نص UTF-8 فقط. يحذف PDF تلقائيًا.

```bash
python3 scripts/materialize_joradp_text.py \
  corpus/texts/DZ-DE-2018-162/sources/sources.yml \
  /tmp/F2018036.txt \
  --lang fr \
  --first-page 7 \
  --last-page 12 \
  --show-resolution
```

لا يحفظ هذا السكربت أي PDF في Git.

## `validate_repository.py`

```bash
python3 scripts/validate_repository.py
```

أو:

```bash
python3 scripts/validate_repository.py /path/to/MFEP_DZ
```

## ما الذي يفحصه الـValidator؟

### التخزين والواجهة البشرية

- منع وجود أي ملف PDF داخل شجرة المستودع؛
- وجود `README.md` بشري لكل حزمة تحت `corpus/texts/`؛
- وجود قسم ظاهر للمصدر الرسمي الأصلي؛
- إذا كان `ar.url` أو `fr.url` معروفًا في `sources.yml`، يجب أن يبقى الرابط المسجل نفسه ظاهرًا في `README.md`؛
- لا يفرض رابطًا عندما تكون قيمة المصدر `null`.

وجود رابط عامل بديل لا يسمح بحذف الرابط المسجل؛ provenance والوصول التشغيلي شيئان مختلفان.

### النصوص المجزأة الأصلية

لكل لغة تحتوي `text/ar/` أو `text/fr/`:

- وجود فهرس لغة؛
- ربط الفهرس جميع الأجزاء؛
- رابط فهرس اللغة داخل كل جزء؛
- رابط العودة إلى `README.md`؛
- السابق/التالي حيث ينطبق.

### النسخ البحثية الموحدة `consolidated/`

كل نسخة موحدة مؤرخة يجب أن تحتوي على الأقل:

- `README.md` مع تنبيه ظاهر بأنها نسخة بحثية وليست نصًا رسميًا مستقلاً؛
- `manifest.yml` يحدد النص الأساس، تاريخ القطع والتعديلات المدمجة؛
- `VERIFICATION.md`؛
- `data/consolidation-map.jsonl`؛
- فهرسي AR/FR وأجزاء النص إذا كان مجزأ.

ويفحص الـValidator كذلك:

- عدم تكرار المادة داخل `consolidation-map.jsonl`؛
- اقتصار عمليات الدمج الحالية على `unchanged`, `amends`, `add_article`؛
- وجود ملفات provenance المشار إليها في `source_segments`, `base_segments`, و`amending_sources`؛
- منع مسارات provenance من الخروج خارج جذر المستودع؛
- روابط السابق/التالي وفهرس اللغة والعودة إلى صفحة النسخة الموحدة داخل كل segment.

### البيانات والـGraph والـEvals

- سلامة JSONL؛
- عدم تكرار معرف النص أو حواف Graph؛
- وجود `record_path`؛
- مطابقة المفردات مع ontology؛
- وسم العقد غير المحلولة؛
- سلامة discovery queue؛
- تطابق Gold Eval cases مع expected outputs.

## الحدود

الـValidator لا يثبت صحة الحكم القانوني، ولا يجعل النسخة الموحدة نصًا رسميًا، ولا يثبت أن endpoint معين سيظل يعمل مستقبلًا. كما أن نجاح خريطة consolidation بنيويًا لا يعني أن دمج كل فقرة صحيح قانونيًا؛ تبقى مراجعة النصوص الأصلية والمعدلة وAR/FR شرطًا مستقلًا.

## CI مستقبلا

```bash
python3 scripts/validate_repository.py
```

ينبغي أن يكون شرطًا أوليًا قبل قبول تغييرات corpus/metadata/graph/consolidated.
