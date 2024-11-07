import fire
import os
import pytest


class Runner(object):
    def __init__(self):
        pass

    def __str__(self):
        return ""

    def rebuild_results_dir(self):
        os.system("rm -rf allure-results")
        os.system("mkdir -p allure-results")
        return self

    def make_history_dir(self):
        if not os.path.exists("allure-results/history"):
            os.system("mkdir -p allure-results/history/")
        return self

    def copy_history_dir(self):
        os.system("cp -r -f allure-report/history/ allure-results/history/")
        return self

    def set_allure_env(self):
        os.system("cp environment.properties allure-results")
        return self

    def generate_allure_report(self):
        os.system("allure generate allure-results -o allure-report --clean")
        return self

    def generate_report(self):
        self.make_history_dir()
        self.copy_history_dir()
        self.set_allure_env()
        self.generate_allure_report()
        self.rebuild_results_dir()
        return self

    def view_report(self):
        os.system("allure serve")
        return self

    def run(self, fast_fail=False, matcher="", cases="", concurrency=1, mark=""):
        args = ["-v", "-s", '--alluredir', "./allure-results"]
        if fast_fail:
            args.append("-x")
        if matcher:
            args.append("-k")
            args.append(matcher)
        if cases:
            if cases is tuple:
                args += cases
            else:
                args += cases.split(",")
        if mark:
            args.append("-m")
            args.append(mark)
        args.append("-n")
        args.append(str(concurrency))
        print(" ".join(args))
        pytest.main(args)
        return self


if __name__ == '__main__':
    fire.Fire(Runner)
