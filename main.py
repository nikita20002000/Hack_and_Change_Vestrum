
class HackAndWin:

    @classmethod
    def show_message(self):
        return 'Мы супер класс, а ты пидорас'

    @classmethod
    def start_work(self):
        import time

        def nick_works():
            for i in range(10):
                time.sleep(2)
                print('Никита работает')

        def lip_works():
            for i in range(10):
                time.sleep(2)
                print('Липарит работает')

        def kate_works():
            for i in range(10):
                time.sleep(2)
                print('Катя работает')

        def andrew_trans():
            for i in range(10):
                time.sleep(2)
                print('Андрей спит')

        try:
            import threading
            a = threading.Thread(target=nick_works)
            b = threading.Thread(target=lip_works)
            c = threading.Thread(target=kate_works)
            d = threading.Thread(target=andrew_trans)

            for i in range(10):
                a.start()
                b.start()
                c.start()
                d.start()
        except:
            return 'Не получается работать'




a = HackAndWin()

print(a.start_work())





