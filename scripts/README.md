# Scripts — deterministic validation

هذه الأدوات **لا تستخدم الذكاء الاصطناعي**. وظيفتها فرض الحد الأدنى من السلامة البنيوية قبل أي ترقية من `staging` إلى `trusted`.

## `validate_repository.py`

تشغيله من جذر نسخة مستنسخة من المستودع:

```bash
python3 scripts/validate_repository.py
```

أو تمرير مسار جذر المستودع:

```bash
python3 scripts/validate_repository.py /path/to/MFEP_DZ
```

## ما الذي يفحصه الإصدار الحالي؟

### التخزين والواجهة البشرية

- منع وجود أي ملف PDF داخل شجرة المستودع؛
- وجود `README.md` بشري لكل حزمة تحت `corpus/texts/`؛
- وجود قسم ظاهر للمصدر الرسمي الأصلي في كل واجهة بشرية؛
- إذا كان رابط PDF العربي أو الفرنسي الأصلي معروفًا في `sources/sources.yml`، يجب أن يظهر الرابط نفسه في `README.md`؛
- لا يفرض رابطًا عندما تكون قيمة المصدر `null`، حتى لا يدفع المشروع إلى اختراع روابط غير متحققة.

### النصوص المجزأة

لكل لغة تحتوي مجلد segments مثل `text/ar/` أو `text/fr/`:

- يجب وجود فهرس لغة `text/ar.md` أو `text/fr.md`؛
- يجب أن يربط الفهرس جميع ملفات الأجزاء؛
- يجب أن يحتوي كل جزء رابطًا إلى فهرس اللغة؛
- يجب أن يحتوي كل جزء رابطًا إلى `README.md` البشري؛
- يجب أن يحتوي الجزء، حيث ينطبق، رابطًا إلى الجزء السابق والجزء التالي.

### البيانات والـGraph والـEvals

- سلامة صيغة كل ملفات JSONL في `metadata/staging/` و`graph/staging/` و`ai/evals/`؛
- عدم تكرار معرف النص القانوني في فهارس staging؛
- وجود `record_path` المشار إليه في metadata؛
- مطابقة `legal_form` و`legal_status` مع `ontology/core.yml`؛
- عدم تكرار معرفات حواف Graph؛
- مطابقة أنواع العلاقات مع ontology؛
- منع حافة إلى `DZ-*` غير معروف ما لم يوسم المصدر/الهدف صراحة بأنه pending أو unresolved؛
- سلامة حالات وأولويات `discovery-queue.jsonl`؛
- عدم تكرار مرشحي Queue؛
- تطابق معرفات Gold Eval cases مع expected outputs.

## حدود الإصدار الحالي

لا يحاول هذا validator تفسير YAML الكامل ولا التحقق من صحة الحكم القانوني نفسه. قراءة `sources.yml` محدودة عمدًا إلى حقلي `ar.url` و`fr.url` ذوي البنية البسيطة الحالية لفرض ظهور المصدر في الواجهة البشرية.

لذلك هو **حاجز بنيوي deterministic gate** وليس بديلا عن:

- JSON Schema المستقبلي؛
- التحقق من المصادر الرسمية؛
- AR/FR alignment؛
- مراجعة العلاقات والحالة القانونية؛
- Gold Evals الخاصة بالذكاء الاصطناعي.

تمت قراءة مفردات `legal_form`, `legal_status`, و`relation_type` مباشرة من `ontology/core.yml` باستخدام البنية البسيطة الحالية دون إضافة dependency خارجية. بعد تثبيت Schema v1 يمكن استبدال/توسيع هذه الآلية بValidator أشد صرامة.

## قاعدة CI المستقبلية

عند إضافة GitHub Actions لاحقا، ينبغي أن يكون نجاح هذا الأمر شرطا أوليا قبل قبول أي تغيير في corpus/metadata/graph:

```bash
python3 scripts/validate_repository.py
```
