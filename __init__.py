from mycroft import MycroftSkill, intent_file_handler


class EasyShoppingSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('skill.shopping.easy.intent')
    def handle_skill_shopping_easy(self, message):
        self.speak_dialog('skill.shopping.easy')


def create_skill():
    return EasyShoppingSkill()

