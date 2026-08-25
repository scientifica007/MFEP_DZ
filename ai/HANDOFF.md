# MFEP_DZ — Handoff

آخر تحديث: 2026-08-25

هذا الملف يعطي أي Agent جديد حالة المشروع الحالية دون الاعتماد على محادثة سابقة.

## المرحلة الحالية

`human_machine_packages_complete_transcription_validation_next`

يوجد 12 سجلا قانونيا في دورة staging/validation، وقد اكتملت هجرتها جميعا إلى حزم دائمة تحت `corpus/texts/` تجمع القراءة البشرية والاستدعاء الآلي. تبقى صفة `staging` مرتبطة بدرجة التحقق، لا بمكان الملف.

## قاعدة التخزين: لا PDF في Git

- لا تحفظ ملفات PDF أو صور صفحات الجريدة الرسمية داخل المستودع.
- `.gitignore` يمنع `*.pdf` و`*.PDF`.
- `scripts/validate_repository.py` يعتبر وجود PDF داخل شجرة المستودع خطأ.
- تحفظ روابط JORADP ورقم الجريدة والصفحات ومحددات اللغة في `sources/sources.yml`.
- إذا احتاج workflow إلى PDF فإنه ينزل مؤقتا، يستخرج النص، ثم يحذف الملف.
- `scripts/materialize_joradp_text.py` يطبق هذا النمط.
- راجع `docs/STORAGE_POLICY.md`.

## نموذج Human + Machine الدائم

لكل نص:

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

- `README.md`: واجهة الباحث/الإنسان.
- `record.yml`: metadata والتصنيف والحالة والتحقق.
- `articles.jsonl`: عنونة واستدعاء المواد للآلة.
- `text/ar.md`, `text/fr.md`: transcription نصية مع حالة صريحة.
- `sources.yml`: source of evidence ولا يحتوي binary.

## حالة الهجرة

تمت هجرة السجلات الـ12 الحالية كلها، مع تحديث metadata إلى المسارات الجديدة وحذف ملفات record القديمة من `corpus/staging/seed-*` حتى لا توجد نسختان دائمتان للحقيقة.

الفهرس البشري: `corpus/INDEX.md`.

## حالة المتن الكامل

**الحزم مكتملة بنيويا، لكن المتون الكاملة ليست كلها متحققة داخليا بعد.**

الحالات المستخدمة تشمل:

- `source_resolution_pending`
- `source_locator_only`
- `transcription_pending`
- `transcribed`
- `verified`

لا يجوز لأي Agent أن يجيب بالنص الداخلي على أنه transcription موثوقة إلا إذا كانت حالة اللغة/المادة `verified`. عند عدم التحقق يرجع إلى المصدر الرسمي وفق المنهج.

`DZ-LAW-2008-007` لديه فهرس كامل للمواد 1–32 مع page locators، لكن text payload الكامل ما زال pending. بقية السجلات لديها حزم موحدة وفهارس مواد جزئية مبنية على ما تم التحقق منه حتى الآن.

## حالة corpus القانونية الحالية

- Graph أولي تحت `graph/staging/`.
- metadata indexes تحت `metadata/staging/` وتشير إلى `corpus/texts/`.
- discovery queue تحت `metadata/discovery-queue.jsonl`.
- Gold Evals أولية للعلاقات القانونية.
- ontology `0.2-draft`.
- 12 حزمة Human + Machine تحت `corpus/texts/`.

## أهم نتائج التصميم

1. Locator النشر مستقل لكل لغة.
2. لا يفضل تضمين القطاع في Canonical ID قبل تثبيت السياسة.
3. الأعمال غير المرقمة تحتاج تاريخ + discriminator؛ لا نخترع أرقاما.
4. relation verification مستقل عن legal-status verification.
5. `status.as_of` ليس `repeal_date`.
6. `interministerial_order` هو المفتاح القانوني للقرار الوزاري المشترك.
7. `provides_for_implementing_act` يختلف عن `enabling_legislation`.
8. النصوص الأفقية تدخل بحسب أثرها على القطاع.
9. النجاح البنيوي في Validator لا يثبت صحة الحكم القانوني.
10. الإنسان والآلة يصلان إلى الكيان نفسه عبر واجهتين، وليس عبر قاعدتي حقيقة منفصلتين.
11. PDF مصدر خارجي لا artifact دائم للمشروع.

## العمل التالي ذو الأولوية

1. إتمام transcription المراجع للقانون 08-07، بدءا بالفرنسية ثم مقابلة العربية وتصحيحها.
2. إدخال text payload إلى `articles.jsonl` أو مراجع segments فقط بعد اعتماد transcription الخاصة بكل مادة.
3. تطبيق نفس materialization والتحقق تدريجيا على السجلات الـ11 الأخرى حسب الأولوية القانونية، لا لمجرد إكمال النصوص.
4. إدخال سلسلة تعديلات القانون 81-07 قبل إلغائه: 90-34، 2000-01، 14-09.
5. إدخال المرسوم 81-392 والنص التطبيقي لسنة 2020 الذي ألغاه.
6. إدخال سلسلة تعديلات 22-70: 22-254، 23-60، 26-87.
7. حسم علاقة 14-140 بالقانون 08-07 على مستوى المادة.
8. توسيع Gold Evals لتشمل transcription/AR-FR alignment والحالة القانونية.
9. اختبار أنواع لم تغط بعد: أمر، مرسوم رئاسي/معاهدة، قرار فردي، تعليمة/منشور، إلغاء جزئي.
10. بعد نضج الحالات تثبيت `legal-text.schema.json` v1.

## ملفات الاستئناف الأساسية

- `corpus/INDEX.md`
- `corpus/texts/README.md`
- `corpus/texts/<TEXT_ID>/README.md`
- `docs/STORAGE_POLICY.md`
- `docs/HUMAN_MACHINE_CORPUS.md`
- `metadata/staging/seed-001.jsonl`
- `metadata/staging/seed-002-dependencies.jsonl`
- `graph/staging/seed-001-relations.jsonl`
- `graph/staging/seed-002-relations.jsonl`
- `metadata/discovery-queue.jsonl`
- `ontology/core.yml`
- `scripts/materialize_joradp_text.py`
- `scripts/validate_repository.py`

## قاعدة الاستئناف

لا توسع corpus لمجرد زيادة العدد. الأولوية الآن لتحويل المصادر الرسمية إلى transcription نصية خفيفة ومراجعة، مع حفظ صريح لدرجة الثقة وعدم إدخال أي PDF. لا يوصف النص الكامل بأنه مخزن داخليا إلا إذا كانت transcription ذات حالة `verified`.
