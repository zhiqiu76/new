class FourDigitYearConverter:
    regex = '[0-9]{4}'

    def to_python(self, value):
        print("路径转化器类：%s" % value)
        return int(value)


    def to_url(self, value):
        print("路径转化器类to_url：%s" % ('%04d' % value))
        return '%04d' % value
