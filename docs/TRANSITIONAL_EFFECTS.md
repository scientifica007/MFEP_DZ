# الأحكام والآثار الانتقالية

## لماذا تحتاج طبقة مستقلة؟

الإلغاء أو التعديل لا يصف دائما الأثر الزمني الكامل للنص. قد يلغي نص جديد نصا سابقا، ثم يبقي بعض النصوص التطبيقية أو المراكز القانونية الناشئة عنه نافذة مؤقتا إلى أن يقع حدث لاحق.

لذلك لا يجوز تمثيل كل حالة من هذا النوع بحافة `repeals` فقط.

## مثال مؤسس من corpus

المادة 14 من المرسوم التنفيذي 16-282:

1. تلغي صراحة المرسوم التنفيذي 09-345؛
2. وتبقي النصوص المتخذة لتطبيق 09-345 سارية المفعول إلى غاية نشر النصوص التطبيقية الجديدة للمرسوم 16-282 في الجريدة الرسمية.

إذن لدينا حدثان قانونيان مختلفان:

```text
16-282#art-14 ──repeals──> 09-345

16-282#art-14
     └── transitional effect:
          implementing texts of 09-345 remain in force
          UNTIL new implementing texts of 16-282 are published
```

## النموذج المقترح

```yaml
transitional_effects:
  - id: TRANS-...
    source_article: art-14
    affected_basis: DZ-DE-2009-345
    subject: implementing_texts_adopted_under_repealed_decree
    effect: remain_in_force_temporarily
    start_event: repeal_of_DZ-DE-2009-345
    end_condition: publication_of_new_implementing_texts_of_DZ-DE-2016-282_in_official_gazette
    explicit: true
    evidence:
      ar: "..."
      fr: "..."
```

## الفرق عن `status`

`status` يصف حالة نص بعينه في تاريخ تقييم محدد.

أما `transitional_effects` فتصف قاعدة زمنية تؤثر على:

- نصوص أخرى؛
- فئة من النصوص التطبيقية؛
- أوضاع قانونية قائمة؛
- مؤسسات أو إجراءات؛
- حقوق أو التزامات تستمر إلى شرط انتهاء معين.

لذلك لا تختزل هذه الآثار في `status: active` أو `repealed`.

## الفرق عن Graph relations

إذا كان الهدف نصا قانونيا محددا، تحفظ علاقة Graph عادية عند إمكان ذلك.

إذا كان الحكم يتناول **مجموعة غير محصورة بعد** مثل «النصوص المتخذة لتطبيقه»، فلا ننشئ عقدا وهمية لكل عنصر ولا ندعي أننا نعرف المجموعة كاملة. نحفظ:

1. علاقة الإلغاء أو التعديل المؤكدة إلى النص المعروف؛
2. `transitional_effects` في السجل المصدر؛
3. evidence؛
4. discovery task لحصر النصوص المتأثرة لاحقا.

عند اكتشاف نص تطبيقي محدد، يمكن ربطه بالأثر الانتقالي بعد التحقق.

## أنواع آثار انتقالية متوقعة

القائمة ليست vocabulary نهائيا، لكنها تشمل على الأقل:

- `remain_in_force_temporarily`
- `continue_until_replacement`
- `continue_until_expiry`
- `grandfather_existing_entities`
- `preserve_existing_rights`
- `preserve_existing_procedures`
- `phase_out_existing_training_cycles`
- `transfer_pending_proceedings`

لا تعتمد قيمة جديدة في trusted schema قبل ظهور حالة مصدرية حقيقية أو حاجة واضحة.

## قواعد التحقق

لا يسجل أثر انتقالي كحقيقة إلا إذا:

- ورد صراحة في نص رسمي؛ أو
- أمكن اشتقاقه من قاعدة قانونية موثقة مع وسمه `derived` لا `explicit`.

يجب حفظ:

- المادة أو الحكم المصدر؛
- موضوع الأثر؛
- بداية الأثر إن أمكن؛
- شرط أو تاريخ انتهائه؛
- اللغة والصفحة أو locator؛
- حالة التحقق.

## أثره على النص الموحد Consolidation

عند بناء نسخة قانونية موحدة مستقبلا، يجب أن يأخذ محرك consolidation الآثار الانتقالية في الحسبان. لا يكفي تطبيق:

```text
old text - repealed provisions + amendments
```

بل قد نحتاج إلى حالة زمنية من نوع:

```text
parent decree = repealed
some implementing acts = temporarily still applicable
```

وهذا أحد أسباب تأجيل consolidated texts إلى مرحلة متقدمة بعد اكتمال graph الزمني.
