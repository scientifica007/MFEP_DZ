# MFEP_DZ — سياق مكثف للذكاء الاصطناعي

## الهوية

- **Jurisdiction:** Algeria / الجزائر
- **Domain:** التكوين والتعليم المهنيين وما يؤثر فيهما أفقيا
- **Purpose:** قاعدة معرفة قانونية وتنظيمية وإدارية موثقة، قابلة للقراءة البشرية والاستدعاء الآلي وبناء Knowledge Graph/RAG فوقها.
- **Persistent memory:** Git repository، لا المحادثة.

## مصدر الحقيقة

الأولوية للمصادر الرسمية، وعلى رأسها:

1. JORADP — الجريدة الرسمية.
2. الأمانة العامة للحكومة.
3. الوزارة والهيئات العمومية المختصة.
4. مصادر رسمية أخرى بحسب الاختصاص.

المصادر الثانوية تساعد في الاكتشاف والفهم، ولا تثبت وحدها نصا رسميا أو حالة قانونية.

## وحدة المعرفة

الوحدة الأساسية هي **النص القانوني/التنظيمي/الإداري**، مع إمكانية النزول إلى المادة والفقرة والبند. ملف PDF وعدد الجريدة الرسمية مصدر نشر وإثبات لا الكيان المنطقي الوحيد.

## النموذج القانوني

لا تستخدم سلما خطيا مبسطا فقط. افصل بين:

- `normative_order`
- `legal_form`
- `legal_function`
- `normative_character`
- `issuing_authority`
- `competence_basis`
- `scope`
- `legal_status`

الدستور، المعاهدات، التشريع، التنظيم، الأعمال الفردية والتفسيرية لا تختزل في اسم الملف.

## اللغات

- `ar`: مسار النشر الرسمي؛ تحقق بصريا عند الشك.
- `fr`: مسار مقابلة واستعادة بنية ومصطلحات عند فساد العربية، مع تسجيل provenance.
- `en`: مساعدة للontology والمصادر الدولية؛ لا تحل محل المصدر الجزائري الرسمي.

لا تنشئ نصا عربيا «رسميا» عبر ترجمة الفرنسية.

## العلاقات المهمة

منها:

`constitutional_basis`, `legal_basis`, `enabling_legislation`, `implements`, `applies`, `amends`, `supplements`, `repeals`, `partially_repeals`, `replaces`, `derogates_from`, `references`, `interprets`, `ratifies`, `approves`.

كل علاقة جوهرية تحتاج evidence. العلاقات العكسية تولد قدر الإمكان.

## الحالة القانونية

لا تستنتج السريان أو الإلغاء بلا دليل. يجب ربط الحالة بـ `status_as_of` وevidence. عند نقص الإثبات استخدم `unknown`.

## طبقات البيانات

احفظ الفصل بين:

`raw → normalized → interpreted`

ومراحل الثقة:

`machine_extracted → structurally_validated → source_checked → cross_language_checked → human_reviewed`

## استراتيجية البناء

ابدأ بـ seed corpus للنصوص المؤسسة، ثم تتبع العلاقات إلى الخلف والأمام (Graph Traversal)، ثم توسع إلى النصوص الأفقية.

## ملفات يجب الرجوع إليها

- `PROJECT_MEMORY.md`
- `docs/LEGAL_SYSTEM_DZ.md`
- `docs/METHODOLOGY.md`
- `docs/LANGUAGE_POLICY.md`
- `docs/DATA_MODEL.md`
- `docs/LEGAL_RELATIONS.md`
- `docs/TAXONOMY.md`
- `docs/SOURCES.md`
- `docs/DECISIONS.md`
- `ai/AGENT_CONTRACT.md`
- `ai/HANDOFF.md`

## ممنوعات سريعة

لا تختلق رقما، تاريخا، مادة، رابطا، علاقة تعديل/إلغاء، أو حالة نفاذ. لا تخف تعارض AR/FR. لا تجعل مخرجات AI المولدة جزءا من trusted corpus بلا تحقق.