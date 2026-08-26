# MFEP_DZ — Handoff

آخر تحديث: 2026-08-26

هذا الملف يعطي أي Agent جديد حالة المشروع الحالية دون الاعتماد على محادثة سابقة.

## المرحلة الحالية

`human_machine_packages_complete_transcription_validation_in_progress`

يوجد 12 سجلا قانونيا في دورة staging/validation، وقد اكتملت هجرتها جميعا إلى حزم دائمة تحت `corpus/texts/`. صفة `staging` أصبحت تعبر عن درجة التحقق القانوني/الزمني، لا عن مكان التخزين.

## قاعدة التخزين: لا PDF في Git

- لا تحفظ ملفات PDF أو صور صفحات الجريدة الرسمية داخل المستودع.
- `.gitignore` يمنع `*.pdf` و`*.PDF`.
- `scripts/validate_repository.py` يعتبر وجود PDF داخل شجرة المستودع خطأ.
- تحفظ روابط JORADP ورقم الجريدة والصفحات ومحددات اللغة في `sources/sources.yml`.
- إذا احتاج workflow إلى PDF فإنه ينزل مؤقتا، يستخرج/يراجع النص، ثم يحذف الملف.
- `scripts/materialize_joradp_text.py` يطبق هذا النمط.

## نموذج Human + Machine

```text
corpus/texts/<TEXT_ID>/
├── README.md
├── record.yml
├── text/
│   ├── ar.md
│   └── fr.md
├── data/
│   └── articles.jsonl
└── sources/
    └── sources.yml
```

يجوز تقسيم لغة طويلة إلى segments، مثل:

```text
text/ar.md
text/ar/01-....md
text/ar/02-....md
```

ويجب أن يشير `articles.jsonl` إلى segment الصحيح لكل مادة.

## حالة transcription الحالية

### DZ-LAW-2008-007 — القانون التوجيهي

- 32 مادة.
- العربية: `verified`.
- الفرنسية: `verified`.
- `articles.jsonl`: 32 مادة مرتبطة بالنسختين المتحققتين.
- هو أول نص ثنائي اللغة متحقق بالكامل داخل Git.
- الحالة القانونية الراهنة للنص ما زالت `unknown` إلى أن ينجز مسح التعديلات/الإلغاءات اللاحقة؛ تحقق المتن لا يساوي تحقق الحالة القانونية.

### DZ-DE-2012-125 — القانون الأساسي النموذجي للـINSFP

- 32 مادة.
- الفرنسية: كاملة `verified`، الصفحات 8–12.
- العربية: كاملة `transcribed`، الصفحات 9–13، ومقسمة إلى ثلاثة segments؛ تحتاج مرور تحقق ثانيا قبل `verified`.
- المادة 1 تطبق المادة 14/الفقرة الأولى من القانون 08-07.
- المادة 31 تلغي صراحة المرسوم 90-235.
- المواد 28–30 تتضمن آثارا انتقالية تتعلق بالملحقات والتكوينات والمعاهد المنشأة في ظل 90-235.
- `DZ-DE-1990-235` أضيف إلى discovery queue بأولوية عالية.

### DZ-DE-2016-282 — التكوين المهني الأولي والشهادات

- 15 مادة.
- العربية: `verified`.
- الفرنسية: `verified`.
- المادة 1 تطبق المادة 19 من القانون 08-07.
- المادة 14 تلغي صراحة المرسوم 09-345.
- المادة 14 تبقي في الوقت نفسه النصوص المتخذة لتطبيق 09-345 سارية مؤقتا إلى غاية نشر النصوص التطبيقية الجديدة لـ16-282.
- لذلك أضيف `transitional_effects` إلى `record.yml` كطبقة مستقلة عن `relations` و`status`.
- `DZ-DE-2009-345` أصبح dependency عالية الأولوية.
- خزن `record.yml` أيضا خريطة أنماط التكوين، مستويات التأهيل الخمسة، ومطابقة المستويات بالشهادات CFPS/CAP/CMP/BT/BTS.

## قواعد استعمال المتن

الحالات المستخدمة تشمل:

- `source_resolution_pending`
- `source_locator_only`
- `transcription_pending`
- `transcribed`
- `verified`

لا يجوز وصف transcription بأنها موثقة نهائيا إلا عند `verified`.

التحقق مستقل لكل لغة؛ يمكن أن تكون الفرنسية `verified` والعربية `transcribed` في النص نفسه.

## آثار انتقالية

راجع `docs/TRANSITIONAL_EFFECTS.md`.

لا تختزل القواعد من نوع «يلغى النص X، غير أن نصوصه التطبيقية تبقى سارية إلى غاية...» في `repeals` فقط. تحفظ:

1. علاقة الإلغاء؛
2. `transitional_effects` مع subject/effect/end_condition/evidence؛
3. مهمة لاكتشاف النصوص التطبيقية المتأثرة إذا لم تكن محصورة بعد.

## حالة Graph والـQueue

- `graph/staging/seed-001-relations.jsonl` يحتوي الآن، ضمن العلاقات المؤكدة، على:
  - 12-125 → implements → 08-07#art-14؛
  - 12-125 → repeals → 90-235؛
  - 16-282 → implements → 08-07#art-19؛
  - 16-282 → repeals → 09-345؛
  - 18-162 → implements → 08-07#art-15؛
  - 20-340 → amends → 18-162؛
  - علاقات 22-70 وقراري 2022/2026؛
  - 26-96 → applies → 12-125#art-3.
- `metadata/discovery-queue.jsonl` يضع الآن 90-235 و09-345 ضمن التبعيات التاريخية عالية الأولوية.

## أهم نتائج التصميم

1. Locator النشر مستقل لكل لغة.
2. القطاع classification وليس جزءا من الهوية القانونية المستقرة مبدئيا.
3. الأعمال غير المرقمة لا يخترع لها رقم.
4. relation verification مستقل عن legal-status verification.
5. `status.as_of` ليس `repeal_date`.
6. `interministerial_order` هو المفتاح المعتمد للقرار الوزاري المشترك.
7. `provides_for_implementing_act` يختلف عن `enabling_legislation`.
8. النصوص الأفقية تدخل بحسب أثرها لا الجهة المصدرة فقط.
9. النجاح البنيوي في Validator لا يثبت صحة الحكم القانوني.
10. PDF مصدر خارجي لا artifact دائم.
11. درجة transcription مستقلة لكل لغة.
12. اللغة الواحدة قد تكون ملفا واحدا أو segments؛ لا يتغير `TEXT_ID`.
13. `articles.jsonl` هو locator/index لا نسخة ثانية من المتن.
14. `repeals` لا يكفي لتمثيل الأحكام الانتقالية؛ نحتاج `transitional_effects`.
15. بيانات بيداغوجية عالية القيمة مثل مستويات التأهيل والشهادات تستخرج إلى حقول منظمة إلى جانب بقاء النص الحرفي.

## العمل التالي ذو الأولوية

1. إجراء المرور الثاني الكامل على العربية لـ12-125 وترقيتها إلى `verified` إذا نجحت المراجعة.
2. إكمال `DZ-DE-2018-162` ثنائي اللغة ثم `DZ-DE-2020-340` لتكوين أول سلسلة أصل + تعديل كاملة النص.
3. حسم علاقة 14-140 بالمادة 14 من 08-07 من الصياغة الكاملة.
4. توسيع Validator للتحقق من:
   - وجود مسارات transcription المذكورة في `articles.jsonl`؛
   - حالات اللغات؛
   - عدد المواد مقابل الفهرس؛
   - segments المعلنة في `record.yml`.
5. إدخال السلفين 90-235 و09-345 عبر Graph Traversal.
6. إدخال سلسلة تعديلات القانون 81-07 قبل إلغائه: 90-34، 2000-01، 14-09.
7. إدخال 81-392 والنص التطبيقي لسنة 2020 الذي ألغاه.
8. إدخال سلسلة تعديلات 22-70: 22-254، 23-60، 26-87.
9. توسيع Gold Evals لتشمل transcription وAR/FR alignment والأحكام الانتقالية.
10. بعد نضج هذه الحالات تثبيت `legal-text.schema.json` v1.

## ملفات الاستئناف الأساسية

- `corpus/INDEX.md`
- `docs/HUMAN_MACHINE_CORPUS.md`
- `docs/TRANSITIONAL_EFFECTS.md`
- `corpus/texts/DZ-LAW-2008-007/`
- `corpus/texts/DZ-DE-2012-125/`
- `corpus/texts/DZ-DE-2016-282/`
- `graph/staging/seed-001-relations.jsonl`
- `metadata/discovery-queue.jsonl`
- `ontology/core.yml`
- `scripts/materialize_joradp_text.py`
- `scripts/validate_repository.py`

## قاعدة الاستئناف

لا توسع corpus لمجرد زيادة العدد. الأولوية الآن لبناء سلاسل قانونية مترابطة كاملة النص والتحقق، وتسجيل كل أثر زمني أو انتقالي دون تبسيطه إلى علاقة واحدة.
