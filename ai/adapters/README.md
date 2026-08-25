# AI Provider Adapters

عند بناء كود يستدعي نماذج ذكاء اصطناعي، يجب عزل تفاصيل المزود داخل adapters بدلا من نشرها في منطق المشروع.

## الواجهة المفاهيمية

```text
AIProvider
  ├── generate_structured(task, context, schema)
  ├── generate_text(task, context)
  └── metadata()
```

يمكن لاحقا توفير تطبيقات مثل:

```text
OpenAIAdapter
AnthropicAdapter
GeminiAdapter
LocalModelAdapter
```

هذه أسماء تنفيذية فقط؛ بقية المشروع لا يجب أن يعتمد عليها مباشرة.

## قواعد

- task contracts تحت `ai/tasks/` مستقلة عن المزود.
- schema والontology لا تتغير لأن مزودا يفضل تنسيقا معينا.
- إعدادات model/provider تحفظ كـrun metadata.
- API keys والأسرار لا تحفظ في Git.
- retry/rate-limit/tool-call formatting مسؤولية adapter لا المنطق القانوني.
- يجب أن تعاد المخرجات إلى تمثيل داخلي موحد قبل validation.

## مثال pseudocode

```python
result = provider.generate_structured(
    task="extract-relations",
    context=context_pack,
    schema=relation_output_schema,
)
validated = validate(result)
```

لا ينبغي أن يحتوي كود `validate()` على شروط من نوع `if provider == ...` إلا لحاجة موثقة استثنائية.

## المبدأ

**Vendor APIs are replaceable infrastructure; legal method is project logic.**
