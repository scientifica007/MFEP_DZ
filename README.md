# MFEP_DZ

قاعدة معرفة قانونية مفتوحة ومهيكلة للنصوص التشريعية والتنظيمية والإدارية المرتبطة بقطاع التكوين والتعليم المهنيين في الجزائر.

الغرض من المستودع ليس جمع ملفات PDF فقط، بل بناء **ذاكرة قانونية قابلة للقراءة البشرية والاستدعاء الآلي** تسمح بمعرفة: ما هو النص؟ من أصدره؟ ما مرتبته ووظيفته القانونية؟ متى نشر ودخل حيز التنفيذ؟ ما النصوص التي يستند إليها؟ ماذا عدّل أو ألغى أو طبّق؟ وما حالته القانونية في تاريخ معين؟

## مبادئ المشروع

1. **المصدر الرسمي أولا**: الجريدة الرسمية والأمانة العامة للحكومة هما المرجع الأول للنصوص المنشورة.
2. **النص القانوني هو وحدة المعرفة**، وليس عدد الجريدة الرسمية أو ملف PDF.
3. **الترتيب القانوني الجزائري شبكة علاقات لا سلم أسماء بسيط**: نفرق بين المرتبة القانونية، شكل النص، الجهة المختصة، الوظيفة القانونية، ومجال الاختصاص.
4. **العربية والفرنسية تعالجان معا**: نعتمد العربية المنشورة رسميا، ونرجع إلى النسخة/الترجمة الفرنسية الرسمية عند فساد الاستخراج العربي أو الحاجة إلى المقابلة المصطلحية، مع التحقق من الصفحة العربية المرئية. الإنجليزية طبقة مساعدة للمفاهيم والأنطولوجيا والمصادر الدولية، وليست بديلا عن المصدر الجزائري الرسمي.
5. **لا نستنتج النفاذ أو الإلغاء بلا دليل**: كل حكم عن الحالة القانونية يجب أن يكون مؤرخا ومدعما بنص أو مادة أو مرجع رسمي.
6. **كل علاقة قانونية يجب أن تكون قابلة للتدقيق**: نميز بين مجرد الإحالة وبين السند الدستوري، سند الاختصاص، التطبيق، التعديل، التتميم، الإلغاء وغيرها.
7. **المستودع هو ذاكرة المشروع**: القرارات المنهجية، المراجع، الافتراضات، المشاكل المعروفة وقواعد العمل توثق هنا ولا تبقى في المحادثات فقط.
8. **طبقة الذكاء الاصطناعي مستقلة عن النموذج والمزود**: يمكن تبديل ChatGPT أو Claude أو Gemini أو نموذج محلي دون تغيير corpus أو ontology أو schema أو الحقيقة القانونية.

## الذاكرة والمنهجية

- [PROJECT_MEMORY.md](PROJECT_MEMORY.md): الذاكرة المركزية للمشروع والقرارات المعتمدة.
- [KNOWLEDGE_CHANGELOG.md](KNOWLEDGE_CHANGELOG.md): سجل تغييرات المعرفة والمنهج.
- [docs/LEGAL_SYSTEM_DZ.md](docs/LEGAL_SYSTEM_DZ.md): النموذج العملي لهيكلة النصوص القانونية والتنظيمية الجزائرية.
- [docs/METHODOLOGY.md](docs/METHODOLOGY.md): طريقة اكتشاف النصوص، استخراجها، التحقق منها وربطها.
- [docs/LANGUAGE_POLICY.md](docs/LANGUAGE_POLICY.md): سياسة العربية والفرنسية والإنجليزية.
- [docs/DATA_MODEL.md](docs/DATA_MODEL.md): نموذج البيانات المقترح لكل نص قانوني.
- [docs/LEGAL_RELATIONS.md](docs/LEGAL_RELATIONS.md): قاموس العلاقات بين النصوص والمواد.
- [docs/TAXONOMY.md](docs/TAXONOMY.md): التصنيف الموضوعي الأولي للقطاع.
- [docs/SOURCES.md](docs/SOURCES.md): سجل المصادر الرسمية والمراجع الأساسية.
- [docs/DECISIONS.md](docs/DECISIONS.md): سجل القرارات المنهجية والمسائل المفتوحة.
- [ontology/core.yml](ontology/core.yml): vocabulary تجريبي قابل للآلة لأشكال النصوص، الوظائف، النطاقات، الحالات والعلاقات.
- [schemas/README.md](schemas/README.md): سياسة تثبيت JSON Schema بعد اختبار corpus حقيقي.

## Corpus التجريبي

بدأ الإدخال الفعلي تحت `corpus/staging/`. يوجد حاليا **12 سجلا قانونيا في staging**؛ لا تعد trusted knowledge بعد.

- [corpus/staging/seed-001/README.md](corpus/staging/seed-001/README.md): العينة الأساسية من 10 نصوص.
- [corpus/staging/seed-002-dependencies/README.md](corpus/staging/seed-002-dependencies/README.md): أول توسع عبر Graph Traversal لحل القانون 81-07 والمرسوم 22-70.
- [metadata/staging/seed-001.jsonl](metadata/staging/seed-001.jsonl) و[metadata/staging/seed-002-dependencies.jsonl](metadata/staging/seed-002-dependencies.jsonl): فهارس آلية مضغوطة.
- [graph/staging/seed-001-relations.jsonl](graph/staging/seed-001-relations.jsonl) و[graph/staging/seed-002-relations.jsonl](graph/staging/seed-002-relations.jsonl): حواف Graph ذات دليل.
- [metadata/discovery-queue.jsonl](metadata/discovery-queue.jsonl): النصوص والتبعيات المكتشفة وحالة معالجتها.

العينة تختبر قوانين مؤسسة وقطاعية، مراسيم تنفيذية تطبيقية ومؤسساتية، نصوصا تعديلية، إنشاء مؤسسات، قرارين وزاريين مشتركين غير مرقمين، ونصا أفقيا صادرا عن قطاع العمل يؤثر مباشرة في التكوين. العلاقات العملية تشمل `implements`, `amends`, `repeals`, `applies`, `provides_for_implementing_act`, و`creates_institution`.

## طبقة الذكاء الاصطناعي

المشروع مصمم ليكون **Model-Agnostic** و**Provider-Agnostic**. الذكاء الاصطناعي أداة استخراج وتحليل فوق المصادر والبيانات، وليس مصدر الحقيقة القانونية.

- [AGENTS.md](AGENTS.md): نقطة دخول عامة لأي Agent أو نموذج جديد.
- [ai/README.md](ai/README.md): معمارية طبقة الذكاء الاصطناعي.
- [ai/AGENT_CONTRACT.md](ai/AGENT_CONTRACT.md): عقد السلوك الموحد وقواعد الإثبات وعدم الاختلاق.
- [ai/PROJECT_CONTEXT.md](ai/PROJECT_CONTEXT.md): سياق مكثف يمكن تحميله للنماذج بسرعة.
- [ai/HANDOFF.md](ai/HANDOFF.md): حالة المشروع الحالية وما يجب تنفيذه لاحقا.
- [ai/context/](ai/context/): سياق وسياسات بصيغة مقروءة آليا.
- [ai/tasks/](ai/tasks/): عقود مهام قياسية مستقلة عن prompts والمزود.
- [ai/evals/](ai/evals/): اختبارات قبول النماذج والـprompts والـpipelines؛ بدأ فيها Gold Corpus فعليا من العلاقات المؤكدة.
- [ai/adapters/](ai/adapters/): سياسة عزل APIs ومزودي النماذج عن المنطق القانوني.

قاعدة التشغيل: **AI output لا يصبح trusted knowledge تلقائيا**. يجب حفظ provenance والدليل والمرور بمراحل التحقق. تغيير النموذج أو prompt لا يمنحه الثقة تلقائيا؛ يُختبر على evals المرجعية قبل استعماله ضمن workflow موثوق.

## المصدر الرسمي الرئيسي

الأمانة العامة للحكومة / الجريدة الرسمية للجمهورية الجزائرية الديمقراطية الشعبية:

- العربية: https://www.joradp.dz/HAR/Accueil.htm
- الفرنسية: https://www.joradp.dz/HFR/Accueil.htm
- البحث المرجعي SCALER: https://www.joradp.dz/SCRIPTS/Joa_Div.dll/RecGet

## حالة المستودع

المشروع في مرحلة **`seed_corpus_staging_validation_and_dependency_expansion`**. تم إدخال 12 نصا، وبناء فهارس وGraph وGold Evals، وتحديث ontology استنادا إلى مشكلات ظهرت في بيانات حقيقية. الأولوية التالية هي استكمال سلسلتي التمهين ومنحة البطالة عبر النصوص المعدلة والتطبيقية، ثم اختبار أنواع قانونية لم تغط بعد قبل تثبيت `legal-text.schema.json` v1.
