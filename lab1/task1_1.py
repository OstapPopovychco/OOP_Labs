class CallReport:
    def gen_report(self, call_data):
        return f"{call_data}"


class RepSaver:
    def save_to_file(self, report_content, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(report_content)
        print(f"Звіт успішно збережено у {filename}")

reporter = CallReport()
saver = RepSaver()

my_calls = reporter.gen_report("Абонент +380934894943, 10:30, 5 хв")

saver.save_to_file(my_calls, "calls.txt")