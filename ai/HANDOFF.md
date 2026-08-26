# MFEP_DZ — Handoff

آخر تحديث: 2026-08-26

## الحالة التشغيلية

`paused_after_DZ-DE-2018-162_completion`

**تعليمة المستخدم الحالية:** تم إكمال المرسوم التنفيذي 18-162. يجب التوقف هنا وعدم الانتقال تلقائيا إلى 20-340 أو أي نص آخر حتى تصدر أوامر جديدة.

## ما اكتمل

- جميع السجلات الحالية لها حزم Human + Machine تحت `corpus/texts/`.
- لا PDF داخل Git؛ الروابط الرسمية فقط تحفظ في `sources.yml`.
- `DZ-LAW-2008-007`: النص العربي والفرنسي الأصليان متحققان.
- `DZ-DE-2016-282`: النص العربي والفرنسي الأصليان متحققان، مع نمذجة إلغاء 09-345 والأثر الانتقالي.
- `DZ-DE-2012-125`: الفرنسية متحققة، والعربية كاملة ومجزأة مع فهرسة 32 مادة.
- `DZ-DE-2018-162`: **اكتمل الآن بالكامل كنص أصلي ثنائي اللغة متحقق.**

## DZ-DE-2018-162 — نقطة التوقف

- العربية: الصفحات الرسمية 7–13، 4 segments، `verified`.
- الفرنسية: الصفحات الرسمية 7–12، 4 segments، `verified`.
- النص الأصلي: 44 مادة مفهرسة في `data/articles.jsonl`.
- المادة 1 تطبق المادة 15 من القانون 08-07.
- المادة 43 تلغي المرسوم 01-419 مع استمرار النصوص التطبيقية القديمة انتقاليا إلى حين صدور نصوص تطبيقية جديدة.
- الحالة القانونية المثبتة: `amended`.
- المرسوم 20-340 يمس المواد 7 و10 و11 و15 و16 و32 و41 ويضيف المادة 35 مكرر.
- transcription الأصلية لم تُعدّل لدمج 20-340؛ `versions.consolidated.available: false`.
- `data/amendment-index.jsonl` و`data/transitional-effects.jsonl` يحفظان هذه الفروق للآلة.
- `VERIFICATION.md` يسجل نطاق التحقق البشري/المصدري.

## Graph وQueue

- أضيفت الحافة `DZ-DE-2018-162 --repeals--> DZ-DE-2001-419` مع وسم الهدف dependency غير محلولة.
- أضيف 01-419 إلى `metadata/discovery-queue.jsonl` بسبب الأثر الانتقالي.
- حافة `DZ-DE-2020-340 --amends--> DZ-DE-2018-162` كانت مثبتة مسبقا وبقيت كما هي.

## قواعد الاستئناف

1. اقرأ `PROJECT_MEMORY.md` و`AGENTS.md` ثم هذا الملف.
2. لا تبدأ 20-340 أو أي نص آخر دون تعليمة جديدة من المستخدم.
3. عند الاستئناف، حافظ على فصل النص الأصلي عن amendment وconsolidated version.
4. لا تدخل PDF أو صور صفحات في Git.
5. استخدم AR/FR معا، وارجع للفرنسية عند فساد الاستخراج العربي مع تحقق بصري من العربية.

## ملفات نقطة التوقف

- `corpus/texts/DZ-DE-2018-162/README.md`
- `corpus/texts/DZ-DE-2018-162/record.yml`
- `corpus/texts/DZ-DE-2018-162/VERIFICATION.md`
- `corpus/texts/DZ-DE-2018-162/text/ar.md`
- `corpus/texts/DZ-DE-2018-162/text/fr.md`
- `corpus/texts/DZ-DE-2018-162/data/articles.jsonl`
- `corpus/texts/DZ-DE-2018-162/data/amendment-index.jsonl`
- `corpus/texts/DZ-DE-2018-162/data/transitional-effects.jsonl`
- `graph/staging/seed-001-relations.jsonl`
- `metadata/discovery-queue.jsonl`

المشروع متوقف هنا بانتظار أوامر المستخدم.
