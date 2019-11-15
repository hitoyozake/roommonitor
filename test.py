# -* encoding: utf-8 *-
import unittest
import post2slack
import monitor


class TestCase(unittest.TestCase):

    def test_commands(self):
        cmdParser = post2slack.CommandParser()
        answer = {"command":"pict", "args":[], "options": ["--a", "--b"]}
        self.assertEqual( answer, cmdParser.parse_token("pict --a --b"))
        pass



if __name__ == '__main__':
    utest = TestCase()

    utest.main()
