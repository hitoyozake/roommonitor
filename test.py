# -* encoding: utf-8 *-
import unittest
import post2slack
import monitor


class TestCase(unittest.TestCase):

    def test_commands(self):
        cmdParser = post2slack.CommandParser()
        answer = {"command":"pictpost", "args":[], "options": ["--a", "--b"]}
        self.assertEqual( answer, cmdParser.parse_rawstring("pictpost --a --b"))
        pass


    def test_get_channnelid(self):
        chid = "C8J45QS8Y"
        client = post2slack.SlackClient(token=chid)

        self.assertNotEqual(client.get_channel_id_by_name("discuss", "general"), None)
        self.assertNotEqual(client.get_channel_message(chid), None)



if __name__ == '__main__':
    utest = TestCase()

    utest.main()
