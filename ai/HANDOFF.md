# MFEP_DZ — Handoff

آخر تحديث: 2026-08-26

## الحالة التشغيلية

`completed_DZ-DE-2020-340_waiting_next_instruction`

## ما اكتمل في الخطوة الأخيرة

تمت معالجة `DZ-DE-2020-340` بوصفه النص المعدل والمتمم للمرسوم `DZ-DE-2018-162`.

### متن 20-340

- عدد المواد: 5.
- الفرنسية: كاملة `verified`، الصفحات 10–12 من الجريدة الرسمية 71/2020.
- العربية: كاملة `transcribed` من طبقة النص الرسمية ومقابلة بالفرنسية؛ تحتاج مرورًا بصريًا عربيًا مستقلاً قبل `verified` بسبب فشل screenshot العربي في هذه الجولة.
- لا PDF داخل Git.
- روابط JORADP وصفحات السنة محفوظة في `sources/sources.yml` والواجهة البشرية.

### خريطة التعديل

- المادة 2 تعدل المواد 7 و10 و11 و15 و16 و32 من 18-162.
- المادة 3 تضيف المادة 35 مكرر.
- المادة 4 تعدل المادة 41.
- المادة 41 الجديدة تمدد مهلة المطابقة من سنة واحدة إلى أربع سنوات، مع استثناء المادة 35 مكرر.

تم إنشاء:

- `corpus/texts/DZ-DE-2020-340/data/amendment-index.jsonl`
- خريطة مقابلة مفصلة داخل `DZ-DE-2018-162/data/amendment-index.jsonl`
- حواف Graph على مستوى المادة.
- Gold Evals جديدة لاستخراج التعديلات المتعددة والإضافة والأثر الانتقالي.

## قاعدة التعديلات والتوحيد

وثقت في `docs/AMENDMENTS_AND_CONSOLIDATION.md` القواعد التالية:

1. transcription الأصلية لا تعدل بعد صدور تعديل لاحق.
2. النص المعدل كيان مستقل.
3. `بدون تغيير / sans changement` تحفظ كما نشرت داخل النص المعدل.
4. لا توسع هذه العبارات تلقائيا داخل transcription.
5. النص الموحد Consolidated Text طبقة بحثية مستقلة ومؤرخة، لا مصدر رسمي بديل.

## نقطة لغوية مفتوحة

في الجملة الختامية للمادة 16 كما عدلها 20-340:

- طبقة النص العربية الرسمية المستخرجة تقرأ: `يسحب قرار الاعتماد`؛
- الفرنسية المتحققة تقرأ: `annule l'arrêté d'agrément`.

لا يحسم المشروع هذا الموضع قبل مرور بصري عربي مستقل. راجع `DZ-DE-2020-340/VERIFICATION.md`.

## روابط JORADP

قاعدة الـresolver ما زالت معتمدة:

- recorded URL لا يحذف عند الفشل؛
- المصدر يحل من `year + issue + language`؛
- `scripts/joradp_resolver.py` و`materialize_joradp_text.py` هما المسار التشغيلي.

## الخطوة المنطقية التالية

بعد إكمال النص الأصلي 18-162 والتعديل 20-340، توجد ثلاثة مسارات ممكنة ويجب اختيار أحدها في التعليمة التالية:

1. **بناء أول نسخة موحدة بحثية مؤرخة لـ18-162 بعد 20-340** لاختبار consolidation؛
2. **العودة إلى Seed Corpus** واستكمال النصوص الناقصة مثل 14-140؛
3. **تتبع سلسلة المؤسسات الخاصة تاريخيًا** بالرجوع إلى 01-419 والنصوص التطبيقية التي أبقاها 18-162 انتقاليا.

لا يبدأ أي من هذه المسارات تلقائيا دون تعليمة المستخدم.

## ملفات نقطة الاستئناف

- `corpus/texts/DZ-DE-2018-162/README.md`
- `corpus/texts/DZ-DE-2018-162/data/amendment-index.jsonl`
- `corpus/texts/DZ-DE-2020-340/README.md`
- `corpus/texts/DZ-DE-2020-340/record.yml`
- `corpus/texts/DZ-DE-2020-340/VERIFICATION.md`
- `corpus/texts/DZ-DE-2020-340/text/ar.md`
- `corpus/texts/DZ-DE-2020-340/text/fr.md`
- `corpus/texts/DZ-DE-2020-340/data/articles.jsonl`
- `corpus/texts/DZ-DE-2020-340/data/amendment-index.jsonl`
- `docs/AMENDMENTS_AND_CONSOLIDATION.md`
- `graph/staging/seed-001-relations.jsonl`
- `ai/evals/cases/seed-001-relation-cases.jsonl`
- `ai/evals/expected/seed-001-relation-expected.jsonl`

المشروع متوقف بعد إكمال 20-340 بانتظار اختيار المسار التالي.
