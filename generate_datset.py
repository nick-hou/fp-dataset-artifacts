import json
import random

if __name__ == '__main__':
    with open('eval_output_adv_merged/merged_data.json', encoding="utf-8") as f:
        merged_data = json.load(f)
        with open("adv_only_shuffled/adv_only_shuffled.json", "w") as outfile:
            for example in merged_data["data"]:
                title = example.get("title", "").strip()
                for paragraph in example["paragraphs"]:
                    context = paragraph["context"].strip()
                    for qa in paragraph["qas"]:
                        question = qa["question"].strip()
                        id_ = qa["id"]

                        if id_.__contains__('high-conf-turk'):
                            *context_og, context_add, _ = context.split('.')
                            context_og.insert(random.randint(0, len(context_og)), context_add)
                            new_context = [s.strip() for s in context_og]
                            new_context = '. '.join(new_context) + '.'

                            answer_starts = [answer["answer_start"] for answer in qa["answers"]]
                            answers = [answer["text"].strip() for answer in qa["answers"]]

                            outfile.write(
                                json.dumps(
                                    {
                                        "title": title,
                                        "context": new_context,
                                        "question": question,
                                        "id": id_,
                                        "answers": {
                                            "answer_start": answer_starts,
                                            "text": answers,
                                        },
                                    }
                                ))
                            # outfile.write(",\n")

