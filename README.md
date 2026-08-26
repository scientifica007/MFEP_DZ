# MFEP_DZ

قاعدة معرفة قانونية مفتوحة ومهيكلة للنصوص التشريعية والتنظيمية والإدارية المرتبطة بقطاع التكوين والتعليم المهنيين في الجزائر.

الغرض من المستودع هو بناء **ذاكرة قانونية قابلة للقراءة البشرية والاستدعاء الآلي** تسمح بمعرفة: ما هو النص؟ من أصدره؟ ما مرتبته ووظيفته القانونية؟ متى نشر ودخل حيز التنفيذ؟ ما النصوص التي يستند إليها؟ ماذا عدّل أو ألغى أو طبّق؟ وما حالته القانونية في تاريخ معين؟

## مبادئ المشروع

1. **المصدر الرسمي أولا**: الجريدة الرسمية والأمانة العامة للحكومة هما المرجع الأول للنصوص المنشورة.
2. **النص القانوني هو وحدة المعرفة**، وليس عدد الجريدة الرسمية أو ملف PDF.
3. **لا تُخزن ملفات PDF في Git**: تحفظ الروابط والمحددات الرسمية، بينما يخزن المشروع مواد نصية خفيفة قابلة للفهرسة والمراجعة. راجع [سياسة التخزين](docs/STORAGE_POLICY.md).
4. **لكل نص واجهتان مترابطتان**: واجهة بشرية `README.md` وواجهة آلة `record.yml` + `articles.jsonl`، مع ملفات transcription نصية مستقلة وحالة تحقق صريحة.
5. **الترتيب القانوني الجزائري شبكة علاقات لا سلم أسماء بسيط**: نفرق بين المرتبة القانونية، شكل النص، الجهة المختصة، الوظيفة القانونية، ومجال الاختصاص.
6. **العربية والفرنسية تعالجان معا**: نعتمد العربية المنشورة رسميا، ونرجع إلى النسخة/الترجمة الفرنسية الرسمية عند فساد الاستخراج العربي أو الحاجة إلى المقابلة المصطلحية، مع التحقق من الصفحة العربية المرئية. الإنجليزية طبقة مساعدة للمفاهيم والأنطولوجيا والمصادر الدولية.
7. **لا نستنتج النفاذ أو الإلغاء بلا دليل**: كل حكم عن الحالة القانونية يجب أن يكون مؤرخا ومدعما بنص أو مادة أو مرجع رسمي.
8. **كل علاقة قانونية يجب أن تكون قابلة للتدقيق**: نميز بين مجرد الإحالة وبين السند الدستوري، سند الاختصاص، التطبيق، التعديل، التتميم، الإلغاء وغيرها.
9. **المستودع هو ذاكرة المشروع**: القرارات المنهجية، المراجع، الافتراضات، المشاكل المعروفة وقواعد العمل توثق هنا ولا تبقى في المحادثات فقط.
10. **طبقة الذكاء الاصطناعي مستقلة عن النموذج والمزود**: يمكن تبديل ChatGPT أو Claude أو Gemini أو نموذج محلي دون تغيير corpus أو ontology أو schema أو الحقيقة القانونية.
11. **رابط JORADP ليس هوية المصدر**: الهوية التشغيلية الثابتة هي السنة + رقم الجريدة + اللغة. يحتفظ المشروع بالرابط المسجل حتى إن تعطل، ويحل endpoint عاملًا عند الحاجة عبر [بروتوكول حل روابط JORADP](docs/JORADP_URL_RESOLUTION.md).
12. **النص الأصلي والتعديل والنص الموحد طبقات منفصلة**: لا يُدمج تعديل لاحق صامتًا داخل transcription الأصلية. راجع [سياسة التعديلات والتوحيد](docs/AMENDMENTS_AND_CONSOLIDATION.md).

## القراءة البشرية للنصوص

- [فهرس corpus البشري](corpus/INDEX.md)
- [المسار الدائم للنصوص](corpus/texts/README.md)

جميع السجلات القانونية الـ12 الحالية لها حزمة موحدة تحت `corpus/texts/`.

البنية الدائمة لكل نص:

```text
corpus/texts/<TEXT_ID>/
├── README.md              # الإنسان
├── record.yml             # بيانات قانونية مهيكلة
├── text/
│   ├── ar.md              # transcription العربية وحالتها
│   └── fr.md              # transcription الفرنسية وحالتها
├── data/
│   └── articles.jsonl     # استدعاء المواد آليا
└── sources/
    └── sources.yml        # روابط ومحددات JORADP وحالة الوصول
```

وقد يحتوي النص المعدل على طبقة ثالثة مستقلة:

```text
consolidated/<CUTOFF_DATE>/
├── README.md
├── manifest.yml
├── VERIFICATION.md
├── data/consolidation-map.jsonl
└── text/{ar,fr}...
```

**تنبيه:** وجود الحزمة لا يعني أن المتن الكامل أصبح متحققًا داخليًا. حالة كل لغة وكل نسخة موحدة معلنة صراحة.

## الذاكرة والمنهجية

- [PROJECT_MEMORY.md](PROJECT_MEMORY.md): الذاكرة المركزية للمشروع والقرارات المعتمدة.
- [KNOWLEDGE_CHANGELOG.md](KNOWLEDGE_CHANGELOG.md): سجل تغييرات المعرفة والمنهج.
- [docs/LEGAL_SYSTEM_DZ.md](docs/LEGAL_SYSTEM_DZ.md): النموذج العملي لهيكلة النصوص القانونية والتنظيمية الجزائرية.
- [docs/METHODOLOGY.md](docs/METHODOLOGY.md): طريقة اكتشاف النصوص، استخراجها، التحقق منها وربطها.
- [docs/LANGUAGE_POLICY.md](docs/LANGUAGE_POLICY.md): سياسة العربية والفرنسية والإنجليزية.
- [docs/STORAGE_POLICY.md](docs/STORAGE_POLICY.md): سياسة التخزين النصي ومنع PDF.
- [docs/HUMAN_MACHINE_CORPUS.md](docs/HUMAN_MACHINE_CORPUS.md): عقد الحزمة المشتركة للإنسان والآلة.
- [docs/JORADP_URL_RESOLUTION.md](docs/JORADP_URL_RESOLUTION.md): حل الروابط المباشرة غير المستقرة مع حفظ provenance.
- [docs/AMENDMENTS_AND_CONSOLIDATION.md](docs/AMENDMENTS_AND_CONSOLIDATION.md): قواعد حفظ النصوص المعدلة وبناء النسخ الموحدة البحثية.
- [docs/DATA_MODEL.md](docs/DATA_MODEL.md): نموذج البيانات المقترح لكل نص قانوني.
- [docs/LEGAL_RELATIONS.md](docs/LEGAL_RELATIONS.md): قاموس العلاقات بين النصوص والمواد.
- [docs/TAXONOMY.md](docs/TAXONOMY.md): التصنيف الموضوعي الأولي للقطاع.
- [docs/SOURCES.md](docs/SOURCES.md): سجل المصادر الرسمية والمراجع الأساسية.
- [docs/DECISIONS.md](docs/DECISIONS.md): سجل القرارات المنهجية والمسائل المفتوحة.
- [ontology/core.yml](ontology/core.yml): vocabulary تجريبي قابل للآلة لأشكال النصوص، الوظائف، النطاقات، الحالات والعلاقات.
- [schemas/README.md](schemas/README.md): سياسة تثبيت JSON Schema بعد اختبار corpus حقيقي.

## Corpus الحالي

يوجد حاليا **12 سجلا قانونيا** في دورة staging/validation، لكنها جميعا تستخدم المسار الدائم `corpus/texts/` للعرض البشري والسجل المهيكل. تبقى صفة `staging` مرتبطة بدرجة التحقق لا بمكان تخزين السجل.

- [corpus/INDEX.md](corpus/INDEX.md): الفهرس البشري لجميع السجلات.
- [metadata/staging/seed-001.jsonl](metadata/staging/seed-001.jsonl) و[metadata/staging/seed-002-dependencies.jsonl](metadata/staging/seed-002-dependencies.jsonl): فهارس آلية تشير إلى الحزم الدائمة.
- [graph/staging/seed-001-relations.jsonl](graph/staging/seed-001-relations.jsonl) و[graph/staging/seed-002-relations.jsonl](graph/staging/seed-002-relations.jsonl): حواف Graph ذات دليل.
- [metadata/discovery-queue.jsonl](metadata/discovery-queue.jsonl): النصوص والتبعيات المكتشفة وحالة معالجتها.

### سلسلة المؤسسات الخاصة المكتملة حتى الآن

- [`DZ-DE-2018-162`](corpus/texts/DZ-DE-2018-162/README.md): النص الأصلي لسنة 2018، AR/FR متحققان.
- [`DZ-DE-2020-340`](corpus/texts/DZ-DE-2020-340/README.md): نص التعديل والتتميم لسنة 2020؛ 5 مواد مفهرسة، الفرنسية متحققة والعربية كاملة `transcribed`، مع خريطة تعديل على مستوى المادة.
- [`DZ-DE-2018-162@consolidated-2020-12-02`](corpus/texts/DZ-DE-2018-162/consolidated/2020-12-02/README.md): **أول نسخة بحثية موحدة فعلية في المشروع**؛ الفرنسية `verified_research_consolidation`، والعربية `provisional_research_consolidation` بسبب نقطة تحقق مفتوحة في المادة 16.

تاريخ القطع في النسخة الموحدة يعني النصوص المدمجة حتى ذلك التاريخ، ولا يعني تلقائيا أنها الحالة القانونية الحالية أو أن تاريخ القطع هو تاريخ النفاذ.

## أدوات الاستخراج والتحقق

- `scripts/joradp_resolver.py`: يحل PDF من هوية العدد، ويجرب الرابط المسجل وبدائل المسار ثم صفحة السنة الرسمية.
- `scripts/materialize_joradp_text.py`: يستخدم الـresolver، يجلب PDF إلى ملف مؤقت فقط، يستخرج النص، ثم يحذف الملف الثنائي.
- `scripts/validate_repository.py`: يفحص البنية، منع PDF، واجهات الإنسان، النصوص المجزأة، والنسخ الموحدة المؤرخة ومسارات provenance الخاصة بها.

هذه الأدوات لا تحول الاستخراج الآلي أو consolidation إلى حقيقة قانونية رسمية؛ transcription والحالة والعلاقات والنسخ الموحدة تبقى خاضعة للتحقق.

## طبقة الذكاء الاصطناعي

المشروع مصمم ليكون **Model-Agnostic** و**Provider-Agnostic**. الذكاء الاصطناعي أداة استخراج وتحليل فوق المصادر والبيانات، وليس مصدر الحقيقة القانونية.

- [AGENTS.md](AGENTS.md): نقطة دخول عامة لأي Agent أو نموذج جديد.
- [ai/README.md](ai/README.md): معمارية طبقة الذكاء الاصطناعي.
- [ai/AGENT_CONTRACT.md](ai/AGENT_CONTRACT.md): عقد السلوك الموحد وقواعد الإثبات وعدم الاختلاق.
- [ai/PROJECT_CONTEXT.md](ai/PROJECT_CONTEXT.md): سياق مكثف يمكن تحميله للنماذج بسرعة.
- [ai/HANDOFF.md](ai/HANDOFF.md): حالة المشروع الحالية وما يجب تنفيذه لاحقا.
- [ai/context/](ai/context/): سياق وسياسات بصيغة مقروءة آليا.
- [ai/tasks/](ai/tasks/): عقود مهام قياسية مستقلة عن prompts والمزود.
- [ai/evals/](ai/evals/): اختبارات قبول النماذج والـprompts والـpipelines، وتشمل الآن اختبارات consolidation.
- [ai/adapters/](ai/adapters/): سياسة عزل APIs ومزودي النماذج عن المنطق القانوني.

قاعدة التشغيل: **AI output لا يصبح trusted knowledge تلقائيا**. يجب حفظ provenance والدليل والمرور بمراحل التحقق.

## المصدر الرسمي الرئيسي

الأمانة العامة للحكومة / الجريدة الرسمية للجمهورية الجزائرية الديمقراطية الشعبية:

- العربية: https://www.joradp.dz/HAR/Accueil.htm
- الفرنسية: https://www.joradp.dz/HFR/Accueil.htm
- البحث المرجعي SCALER: https://www.joradp.dz/SCRIPTS/Joa_Div.dll/RecGet

## حالة المستودع

المشروع في حالة **`completed_first_consolidation_DZ-DE-2018-162_2020-12-02`**. أول نسخة بحثية موحدة مؤرخة أصبحت متاحة وقابلة للقراءة والاستدعاء الآلي. الخطوة المنطقية الأقوى تاليا هي forward search بعد 2 ديسمبر 2020 للتحقق من أي تعديلات لاحقة قبل وصف نسخة ما بأنها أحدث حالة قانونية؛ راجع `ai/HANDOFF.md`.
