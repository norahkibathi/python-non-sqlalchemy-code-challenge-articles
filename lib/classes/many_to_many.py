class Article:
#the code enables sotring of all instances of the class article 
    all = []

    def __init__(self, author, magazine, title):
        #the code enables provision of all attributes in the class of article 
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)
        
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        #the code checks whether the tittle is between 5-50 string
        if isinstance(title, str) and 5 <= len(title) <= 50 and not hasattr(self, 'title'):
            self._title =name

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine
      

class Author:
    #the class enables passing of author aurgements into the code with the init method declaring the attributes in the code 
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        #ensures that the name  attribute is not empty
        if isinstance(name, str) and name != "" and not hasattr(self, 'name'):
            self._name = name
        
    def articles(self):
        #defines the articles method and uses list comprehension to iterate all of the articles in Article.all list
       
        return [article for article in Article.all if article._author == self]

    def magazines(self):
        return list({article._magazine for article in Article.all if article._author == self})

    def add_article(self, magazine, title):
        #the method adds a new article containing article tittle ,aurthor and magazine
        return Article(self, magazine, title)

    def topic_areas(self):
        #the code enables returing a list of article 's topics areas written by the author and incase it has no author it returns none
        topics = list({article._magazine.category for article in Article.all if article._author == self})
        return topics if topics else None

class Magazine:
    all = [] #code enables sotring of all instances of the class Magazine
    def __init__(self, name, category):
       # the code enables intialization of attributes of the class 
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    #the code checks whether the name used is a string and has a lenght between 2-16
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        
    
        

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        #the code checks whether the category is a string and is not empty
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        


    def articles(self):
        return [article for article in Article.all if article._magazine == self]

    def contributors(self):
        return list({article._author for article in Article.all if article._magazine == self})

    def article_titles(self):
        #the fucntion allows retruning a list of all the articles titles
        titles = [article._title for article in Article.all if article._magazine == self]
        return titles if titles else None

    def contributing_authors(self):
    #contributing_authors first initializes an empty dictionary called author_article_count
    #It then iterates over the articles associated with the instance and checks
    #if the author of each article is an instance of the Author class.
    #If so, it updates the count of articles for that author in the author_article_count dictionary.
    # After that, it creates a list of authors who have contributed more than 2 articles
    # by filtering the author_article_count dictionary it returns the list of contributing authors or None if there are no contributing authors.
        authors = [article._author for article in Article.all if article._magazine == self]
        contributors = list({author for author in authors if authors.count(author) > 2})
        return contributors if contributors else None