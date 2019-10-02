import random

class Model():

    def __init__(self):
        self.train_list = []
        self.train_label = []
        self.test_list = []
        self.test_label = []
        self.pred = []
        self.knowledge = {}
        self.feature_name = []


    def prediction(self):
        if not self.pred:
            print("The AI don't have do any train, please train it "
                  "before use their prediction using `train()` function")
            if not self.train_list:
                print("\nYou don't even have parse your data, "
                      "please use `split_train_and_test()` function")
        else:
            print("The list of data that was tested", self.test_list)
            print("The list of prediction for each data", self.pred)


    def get_data(self, feature_name):
        """
        Function to get some data.
        Take the name of the feature to stock them into the model
        """
        if not check(feature_name, []):
            exit(84)
        self.feature_name = feature_name


    def org_data(self, data=None, label=None):
        """
        Get data in input and organize them by returning all data inside
        """
        if not data or not label:
            print("Be careful !!\nYou don't have initialized your data in the model, "
                  "be sure to pass it in next functions you'll use")
        self.data = data
        self.label = label
        return None

    def train(self):
        """
        It's the function used to train our model and return it save
        """
        length = len(self.train_list)
        i = 0
        while i < length:
            self.knowledge.update({self.train_list[i]: self.train_label[i]})
            i += 1


    def test_model_prediction(self, k=3):
        """
        Test our model and add his prediction in the self.pred list
        arg = k is k=3 by default but can be change, it's the accuracy
        of the aglorythm
        """
        if not check(k, 0):
            exit(84)
        for each in self.test_list:
            can_naive = False
            for elem in self.knowledge:
                if each == elem:
                    can_naive = True
                    break
            if can_naive:
                self.__algorythm_naive__(each)
            else:
                self.__algorythm_knn__(each, k)


    def accuracy(self, repeat=1):
        """
        Get the accuracy of our model, can get a number 
        to have a better accuracy precision.\n
        You can repeat any number of time but the program will take more time
        """
        if not check(repeat, 0):
            exit(84)
        accur = 0
        total = 0
        i = 0
        while repeat >= 1:
            for elem in self.test_label:
                if elem == self.pred[i]:
                    accur += 1
                total += 1
                i += 1
            repeat -= 1
            i = 0
        total_accuracy = accur / total * 100
        if total_accuracy >= 50:
            COLOR = "\x1b[32m"
        else:
            COLOR = "\x1b[31m"
        print("The accuracy of the algorythm is " + COLOR + str(total_accuracy) + "%")


    def split_train_and_test(self, data=None, label=None, train_size=0.5):
        """
        Split all data into a test model and a train model.\n
        Parameter:\n
        Data: All the data that will be split according to a random variable. (list)\n
        Label: The True label of the different data. (list)\n

        After use this function, you'll have access to the four list belowing:
            self.train_list
            self.train_label
            self.test_list
            self.test_label
        """
        if not data:
            data = self.data
        if not label:
            label = self.label
        if not label or not data:
            print("Don't have any data to parse")
            exit(84)
        self.org_data(data, label)
        weight = len(data) * train_size
        while weight > 0:
            rand = randomisation(0, len(data))
            is_present = True
            while is_present:
                is_present = False
                for each in self.train_list:
                    if each == data[rand]:
                        is_present = True
                        rand = randomisation(0, len(data))
            self.train_list.append(data[rand])
            self.train_label.append(label[rand])
            weight -= 1
        i = 0
        while i < len(data):
            is_present = False
            for each in self.train_list:
                if each == data[i]:
                    is_present = True
            if not is_present:
                self.test_list.append(data[i])
                self.test_label.append(label[i])
            i += 1


    def __algorythm_naive__(self, main_element):
        """
        First part of our algorythm, Naives Bayes
        """
        if not check(main_element, []):
            exit(84)
        how_many = {}
        who = []
        exist = False
        for each in self.knowledge:
            if each == main_element:
                for me in who:
                    if each == me:
                        exist = True
                        break
                if not exist:
                    who.append(each)
                if not how_many[each]:
                    how_many.update(each, 1)
                else:
                    how_many[each] += 1

        stock = 0
        index = 0
        i = 0
        for nb in how_many:
            if stock < nb:
                stock = nb
                index = i
            i += 1
        self.pred.append(who.index(index))
        return None


    def __algorythm_knn__(self, main_element, k):
        """
        Second part of our algorythm, K-nearest-neightbour
        """
        if not check(main_element, ""):
            exit(84)
        if not check(k, 0):
            exit(84)
        neightbour = {}
        k_in = 0
        i = 0
        each_tmp_less = 0
        each_tmp_more = 0
        count = 1
        main_element = main_element.strip('][').split(', ')
        for each in main_element:
            neightbour.update({self.feature_name[i]: []})
            while k_in <= k:
                if count == 1:
                    each_tmp_more = int(each)
                for elem in self.knowledge:
                    elem = elem.strip('][').split(', ')
                    if int(elem[i]) == each_tmp_more:
                        k_in += 1
                        if k_in > k:
                            break
                        neightbour[self.feature_name[i]].append(elem)
                if k_in > k:
                    break
                each_tmp_more = int(each) + count
                if count == 1:
                    each_tmp_less = int(each)
                for elem in self.knowledge:
                    elem = elem.strip('][').split(', ')
                    if int(elem[i]) == each_tmp_less:
                        k_in += 1
                        if k_in > k:
                            break
                        neightbour[self.feature_name[i]].append(elem)
                if k_in > k:
                    break
                each_tmp_less = int(each) - count

                count += 1
            i += 1
            k_in = 0
        self.__res_knn_algo__(neightbour, main_element)
        return None


    def __res_knn_algo__(self, neightbour, main_element):
        """
        Result of the K-nearest-neightbour algorythm
        """
        list_of_proba = []
        is_alive_count = 0
        is_dead_count = 0
        for elem in neightbour:
            i = 0
            for each in neightbour[elem]:
                neightbour[elem][i] = str(each).replace("'", "")
                i += 1
        for feature in self.feature_name:
            for elem in neightbour[feature]:
                list_of_proba.append(self.knowledge[elem])
        for nb in list_of_proba:
            if nb == 1:
                is_alive_count += 1
            if nb == 0:
                is_dead_count += 1
        if is_alive_count > is_dead_count:
            self.pred.append(1)
        if is_alive_count <= is_dead_count:
            self.pred.append(0)


def randomisation(min, max):
    min_tmp = min
    while min_tmp < max:
        tmp = int(random.uniform(min, max))
        min_tmp += tmp / 2
    return tmp


def check(var, type_obj):
    """
    Check if a var is type of type_obj or not
    type_obj will be a empty var of the type needed to check
    Return True or False

    ex:
        check("I am a string", "") ----------- True
        check(["I", "am", "a", "list"], []) -- True
        check(42, 0) ------------------------- True
        check("I am not a dict", {}) --------- False
    """
    if type(var) == type(type_obj):
        return True
    print(var, "is not type of", \
        str(type(type_obj)).replace('<class ', '').replace('>', ''))
    return False