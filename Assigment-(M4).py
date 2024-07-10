class book:
    def __init__(self,titl,auth,pub,prc,ar):
        self.title=titl
        self.author=auth
        self.publisher=pub
        self.price=int(prc)
        self.author_royalty=int(ar)
        
    def get_book(self):
        return "Title: {}\n Author: {}\n Publisher: {}\n Price:{} \n Author Royalty: {}".format(self.title,self.author,self.publisher,self.price,self.author_royalty)
        
    def set_book(self,titl,auth,pub,prc,ar):
        self.title=titl
        self.author=auth
        self.publisher=pub
        self.price=prc
        self.author_royalty=ar
        return
        
    def royalty(self,copy):
        if copy<=500:
            return (self.price*copy*0.10)
        
        elif copy<=1500:
            return (self.price*500*0.10)+(self.price*(copy-500)*0.125)
        
        else:
            return (self.price*500*0.10)+(self.price*1000*0.125)+(self.price*(copy-1500)*0.15)
   
        
class ebook (book):
    
    def __init__(self,titl,auth,pub,prc,ar,form):
        super().__init__(titl,auth,pub,prc,ar)
        self.format=form
    
    def royalty(self,copy):
        new_royalty=super().royalty(copy)
        gst_deduction=new_royalty*0.12
        return (new_royalty-gst_deduction)
        
