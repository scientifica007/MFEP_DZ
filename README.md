# MFEP_DZ

قاعدة معرفة قانونية مفتوحة ومهيكلة للنصوص التشريعية والتنظيمية والإدارية المرتبطة بقطاع التكوين والتعليم المهنيين في الجزائر.

الغرض من المستودع هو بناء **ذاكرة قانونية قابلة للقراءة البشرية والاستدعاء الآلي** تسمح بمعرفة: ما هو النص؟ من أصدره؟ ما مرتبته ووظيفته القانونية؟ متى نشر ودخل حيز التنفيذ؟ ما النصوص التي يستند إليها؟ ماذا عدّل أو ألغى أو طبّق؟ وما حالته القانونية في تاريخ معين؟

## مبادئ المشروع

1. **المصدر الرسمي أولا**: الجريدة الرسمية والأمانة العامة للحكومة هما المرجع الأول للنصوص المنشورة.
2. **النص القانوني هو وحدة المعرفة**، وليس عدد الجريدة الرسمية أو ملف PDF.
3. **لا تُخزن ملفات PDF في Git**: تحفظ الروابط والمحددات الرسمية، بينما يخزن المشروع مواد نصية خفيفة قابلة للفهرسة والمراجعة. راجع [سياسة التخزين](docs/STORAGE_POLICY.md).
4. **لكل نص واجهتان مترابطتان**: واجهة بشرية `README.md` وواجهة آلة `record.yml` + `articles.jsonl`، مع ملفات transcription نصية مستقلة عند اكتمالها.
5. **الترتيب القانوني الجزائري شبكة علاقات لا سلم أسماء بسيط**: نفرق بين المرتبة القانونية، شكل النص، الجهة المختصة، الوظيفة القانونية، ومجال الاختصاص.
6. **العربية والفرنسية تعالجان معا**: نعتمد العربية المنشورة رسميا، ونرجع إلى النسخة/الترجمة الفرنسية الرسمية عند فساد الاستخراج العربي أو الحاجة إلى المقابلة المصطلحية، مع التحقق من الصفحة العربية المرئية. الإنجليزية طبقة مساعدة للمفاهيم والأنطولوجيا والمصادر الدولية.
7. **لا نستنتج النفاذ أو الإلغاء بلا دليل**: كل حكم عن الحالة القانونية يجب أن يكون مؤرخا ومدعما بنص أو مادة أو مرجع رسمي.
8. **كل علاقة قانونية يجب أن تكون قابلة للتدقيق**: نميز بين مجرد الإحالة وبين السند الدستوري، سند الاختصاص، التطبيق، التعديل، التتميم، الإلغاء وغيرها.
9. **المستودع هو ذاكرة المشروع**: القرارات المنهجية، المراجع، الافتراضات، المشاكل المعروفة وقواعد العمل توثق هنا ولا تبقى في المحادثات فقط.
10. **طبقة الذكاء الاصطناعي مستقلة عن النموذج والمزود**: يمكن تبديل ChatGPT أو Claude أو Gemini أو نموذج محلي دون تغيير corpus أو ontology أو schema أو الحقيقة القانونية.

## القراءة البشرية للنصوص

- [فهرس corpus البشري](corpus/INDEX.md)
- [المسار الدائم للنصوص](corpus/texts/README.md)
- أول نص مهاجر إلى النموذج الدائم: [القانون 08-07](corpus/texts/DZ-LAW-2008-007/README.md)

البنية الدائمة لكل نص:

```text
corpus/texts/<TEXT_ID>/
├── README.md              # الإنسان
├── record.yml             # بيانات قانونية مهيكلة
├── text/
│   ├── ar.md              # transcription العربية
│   └── fr.md              # transcription الفرنسية
├── data/
│   └── articles.jsonl     # استدعاء المواد آليا
└── sources/
    └── sources.yml        # روابط ومحددات JORADP
```

لا يعني وجود مجلد النص أن transcription الكامل متحقق؛ حالة كل لغة مصرح بها في `record.yml` وملف اللغة نفسه.

## الذاكرة والمنهجية

- [PROJECT_MEMORY.md](PROJECT_MEMORY.md): الذاكرة المركزية للمشروع والقرارات المعتمدة.
- [KNOWLEDGE_CHANGELOG.md](KNOWLEDGE_CHANGELOG.md): سجل تغييرات المعرفة والمنهج.
- [docs/LEGAL_SYSTEM_DZ.md](docs/LEGAL_SYSTEM_DZ.md): النموذج العملي لهيكلة النصوص القانونية والتنظيمية الجزائرية.
- [docs/METHODOLOGY.md](docs/METHODOLOGY.md): طريقة اكتشاف النصوص، استخراجها، التحقق منها وربطها.
- [docs/LANGUAGE_POLICY.md](docs/LANGUAGE_POLICY.md): سياسة العربية والفرنسية والإنجليزية.
- [docs/STORAGE_POLICY.md](docs/STORAGE_POLICY.md): سياسة التخزين النصي ومنع PDF.
- [docs/DATA_MODEL.md](docs/DATA_MODEL.md): نموذج البيانات المقترح لكل نص قانوني.
- [docs/LEGAL_RELATIONS.md](docs/LEGAL_RELATIONS.md): قاموس العلاقات بين النصوص والمواد.
- [docs/TAXONOMY.md](docs/TAXONOMY.md): التصنيف الموضوعي الأولي للقطاع.
- [docs/SOURCES.md](docs/SOURCES.md): سجل المصادر الرسمية والمراجع الأساسية.
- [docs/DECISIONS.md](docs/DECISIONS.md): سجل القرارات المنهجية والمسائل المفتوحة.
- [ontology/core.yml](ontology/core.yml): vocabulary تجريبي قابل للآلة لأشكال النصوص، الوظائف، النطاقات، الحالات والعلاقات.
- [schemas/README.md](schemas/README.md): سياسة تثبيت JSON Schema بعد اختبار corpus حقيقي.

## Corpus التجريبي

يوجد حاليا **12 سجلا قانونيا** في دورة staging/validation. بدأ نقلها من النموذج التجريبي إلى `corpus/texts/`، وأول سجل مهاجر فعليا هو `DZ-LAW-2008-007`.

- [corpus/INDEX.md](corpus/INDEX.md): الحالة البشرية لكل سجل وهجرته.
- [corpus/staging/seed-001/README.md](corpus/staging/seed-001/README.md): العينة الأساسية.
- [corpus/staging/seed-002-dependencies/README.md](corpus/staging/seed-002-dependencies/README.md): أول توسع عبر Graph Traversal.
- [metadata/staging/seed-001.jsonl](metadata/staging/seed-001.jsonl) و[metadata/staging/seed-002-dependencies.jsonl](metadata/staging/seed-002-dependencies.jsonl): فهارس آلية مضغوطة.
- [graph/staging/seed-001-relations.jsonl](graph/staging/seed-001-relations.jsonl) و[graph/staging/seed-002-relations.jsonl](graph/staging/seed-002-relations.jsonl): حواف Graph ذات دليل.
- [metadata/discovery-queue.jsonl](metadata/discovery-queue.jsonl): النصوص والتبعيات المكتشفة وحالة معالجتها.

## أدوات الاستخراج والتحقق

- `scripts/materialize_joradp_text.py`: يجلب PDF الرسمي إلى ملف مؤقت فقط، يستخرج النص، ثم يحذف الملف الثنائي.
- `scripts/validate_repository.py`: يتحقق من البنية ويفشل إذا وجد أي ملف PDF داخل شجرة المستودع.

هذه الأدوات لا تحول الاستخراج الآلي إلى حقيقة قانونية؛ transcription والحالة والعلاقات تبقى خاضعة للتحقق.

## طبقة الذكاء الاصطناعي

المشروع مصمم ليكون **Model-Agnostic** و**Provider-Agnostic**. الذكاء الاصطناعي أداة استخراج وتحليل فوق المصادر والبيانات، وليس مصدر الحقيقة القانونية.

- [AGENTS.md](AGENTS.md): نقطة دخول عامة لأي Agent أو نموذج جديد.
- [ai/README.md](ai/README.md): معمارية طبقة الذكاء الاصطناعي.
- [ai/AGENT_CONTRACT.md](ai/AGENT_CONTRACT.md): عقد السلوك الموحد وقواعد الإثبات وعدم الاختلاق.
- [ai/PROJECT_CONTEXT.md](ai/PROJECT_CONTEXT.md): سياق مكثف يمكن تحميله للنماذج بسرعة.
- [ai/HANDOFF.md](ai/HANDOFF.md): حالة المشروع الحالية وما يجب تنفيذه لاحقا.
- [ai/context/](ai/context/): سياق وسياسات بصيغة مقروءة آليا.
- [ai/tasks/](ai/tasks/): عقود مهام قياسية مستقلة عن prompts والمزود.
- [ai/evals/](ai/evals/): اختبارات قبول النماذج والـprompts والـpipelines.
- [ai/adapters/](ai/adapters/): سياسة عزل APIs ومزودي النماذج عن المنطق القانوني.

قاعدة التشغيل: **AI output لا يصبح trusted knowledge تلقائيا**. يجب حفظ provenance والدليل والمرور بمراحل التحقق.

## المصدر الرسمي الرئيسي

الأمانة العامة للحكومة / الجريدة الرسمية للجمهورية الجزائرية الديمقراطية الشعبية:

- العربية: https://www.joradp.dz/HAR/Accueil.htm
- الفرنسية: https://www.joradp.dz/HFR/Accueil.htm
- البحث المرجعي SCALER: https://www.joradp.dz/SCRIPTS/Joa_Div.dll/RecGet

## حالة المستودع

المشروع في مرحلة **`seed_corpus_staging_validation_and_human_machine_migration`**. بدأ تحويل corpus إلى حزم نصية تجمع القراءة البشرية والاستدعاء الآلي، مع منع PDF نهائيا داخل Git. الأولوية الحالية هي إتمام نقل النصوص الـ12، ثم اعتماد transcriptionات النصية المراجعة وبناء Schema v1 على ما تعلمناه من الحالات الحقيقية.
