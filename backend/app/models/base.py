from sqlalchemy.ext.declarative import as_declarative, declared_attr
#as_declarative: Transforma uma classe em uma classe base declarativa do SQLAlchemy
#declared_attr: Permite que um método de classe seja tratado como um atributo, útil para definir automaticamente valores para todas as subclasses.

@as_declarative()
class Base:
    id: any
    __name__: str
    
    #Esse método gera automaticamente o nome da tabela baseado no nome da classe.
    @declared_attr
    def __tablename__(cls) -> str:

        #Converte o nome da classe para minúsculas para ser usado como nome da tabela.
        return cls.__name__.lower()

