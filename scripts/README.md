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

مثال من سجل مصدر:

```bash
python3 scripts/joradp_resolver.py \
  corpus/texts/DZ-DE-2018-162/sources/sources.yml \
  --lang fr \
  --json
```

أو من رابط مباشر قديم:

```bash
python3 scripts/joradp_resolver.py \
  https://www.joradp.dz/FTP/jo-francais/2018/F2018036.pdf \
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

تشغيله من جذر نسخة مستنسخة من المستودع:

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

### النصوص المجزأة

لكل لغة تحتوي `text/ar/` أو `text/fr/`:

- وجود فهرس لغة؛
- ربط الفهرس جميع الأجزاء؛
- رابط فهرس اللغة داخل كل جزء؛
- رابط العودة إلى `README.md`؛
- السابق/التالي حيث ينطبق.

### البيانات والـGraph والـEvals

- سلامة JSONL؛
- عدم تكرار معرف النص أو حواف Graph؛
- وجود `record_path`؛
- مطابقة المفردات مع ontology؛
- وسم العقد غير المحلولة؛
- سلامة discovery queue؛
- تطابق Gold Eval cases مع expected outputs.

## الحدود

الـValidator لا يثبت صحة الحكم القانوني ولا أن endpoint معين سيظل يعمل في المستقبل. والـresolver لا يثبت بدوره صحة مضمون العدد. بعد الوصول يجب التحقق من هوية الجريدة والنص والصفحات وفق منهج المشروع.

## CI مستقبلا

```bash
python3 scripts/validate_repository.py
```

ينبغي أن يكون شرطًا أوليًا قبل قبول تغييرات corpus/metadata/graph.
