# -*- coding: utf-8 -*-
"""This file is part of the Daliegest project.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
__author__ = 'Francesco Marella <francesco.marella@anche.no>'
__copyright__ = 'Copyright © 2014 Francesco Marella'

from flask_application import app

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import UserMixin, RoleMixin

from datetime import datetime
from sqlalchemy_utils import generic_relationship
from sqlalchemy_utils import LocaleType, ChoiceType, ScalarListType, TimezoneType, Choice
#from babel import Locale


db = SQLAlchemy(app)

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer, db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    locale = db.Column(LocaleType)
    timezone = db.Column(TimezoneType(backend='pytz'))
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))

class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    provider_id = db.Column(db.String(255))
    provider_user_id = db.Column(db.String(255))
    access_token = db.Column(db.String(255))
    secret = db.Column(db.String(255))
    display_name = db.Column(db.String(255))
    profile_url = db.Column(db.String(512))
    image_url = db.Column(db.String(512))
    rank = db.Column(db.Integer)

class Banca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    denominazione = db.Column(db.String(200), nullable=False, unique=True)
    agenzia = db.Column(db.String(200), nullable=False, unique=True)
    iban = db.Column(db.String(30))
    abi = db.Column(db.String(5))
    cab = db.Column(db.String(5))
    bic_swift = db.Column(db.String(200))

class CategoriaArticolo(db.Model):
    __tablename__ = 'categoria_articolo'
    id = db.Column(db.Integer, primary_key=True)
    denominazione = db.Column(db.String(200))

class CategoriaFornitore(db.Model):
    __tablename__ = 'categoria_fornitore'
    id = db.Column(db.Integer, primary_key=True)
    denominazione = db.Column(db.String(200))

class AliquotaIva(db.Model):
    __tablename__ = 'aliquota_iva'
    id = db.Column(db.Integer, primary_key=True)
    denominazione = db.Column(db.String(200))
    percentuale = db.Column(db.Numeric(8,4))

class Pagamento(db.Model):
    __tablename__ = 'pagamento'
    TIPI = [
        ('banca', 'Banca'),
        ('cassa', 'Cassa')
    ]
    id = db.Column(db.Integer, primary_key=True)
    denominazione = db.Column(db.String(200))
    tipo = db.Column(ChoiceType(TIPI))
    scadenza_rate = db.Column(ScalarListType(int))
    fine_mese = db.Column(db.Boolean, default=False)
    aliquota_iva_id = db.Column(db.Integer, db.ForeignKey('aliquota_iva.id'))
    aliquota_iva = db.relationship('AliquotaIva')

persona_giuridica_sede = db.Table('persona_giuridica_sede',
    db.Column('sede_id', db.Integer, db.ForeignKey('sede.id')),
    db.Column('persona_giuridica_id', db.Integer, db.ForeignKey('persona_giuridica.id')))

class Sede(db.Model):
    __tablename__ = 'sede'
    TIPI = [
        ('operativa', 'Operativa'),
        ('legale', 'Legale'),
        ('magazzino', 'Magazzino'),
        ('altro', 'Altro')
    ]
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(ChoiceType(TIPI))
    indirizzo = db.Column(db.String(300))
    cap = db.Column(db.String(10))
    provincia = db.Column(db.String(50))
    localita = db.Column(db.String(200))
    nazione = db.Column(db.String(200))

class Magazzino(db.Model):
    __tablename__ = 'magazzino'
    id = db.Column(db.Integer, primary_key=True)
    denominazione = db.Column(db.String(200))
    codice = db.Column(db.String(10))
    sede_id = db.Column(db.Integer, db.ForeignKey('sede.id'))
    sede = db.relationship('Sede')

class PersonaGiuridica(db.Model):
    __tablename__ = 'persona_giuridica'
    id = db.Column(db.Integer, primary_key=True)
    codice = db.Column(db.String(50))
    ragione_sociale = db.Column(db.String(200))
    nome = db.Column(db.String(100))
    cognome = db.Column(db.String(100))
    codice_fiscale = db.Column(db.String(16))
    partita_iva = db.Column(db.String(30))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    note = db.Column(db.Text)
    cancellato = db.Column(db.Boolean(), default=False)
    sedi = db.relationship('Sede', secondary=persona_giuridica_sede,
                            backref=db.backref('pg', lazy='dynamic'))

class Cliente(db.Model):
    __tablename__ = 'cliente'
    TIPI = [
        ('pg', 'Persona giuridica'),
        ('pf', 'Persona fisica'),
    ]
    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(ChoiceType(TIPI))
    pagamento_id = db.Column(db.Integer, db.ForeignKey('pagamento.id'))
    aliquota_iva_id = db.Column(db.Integer, db.ForeignKey('aliquota_iva.id'))
    banca_id = db.Column(db.Integer, db.ForeignKey('banca.id'))
    magazzino_id = db.Column(db.Integer, db.ForeignKey('magazzino.id'))
    listino_id = db.Column(db.Integer, db.ForeignKey('listino.id'))
    listino = db.relationship('Listino')
    #escusione_spese

    def as_dict(self):
        s = dict()
        for c in self.__table__.columns:
            if isinstance(getattr(self, c.name), Choice):
                v = getattr(self, c.name).value
            else:
                v = getattr(self, c.name)
            s[c.name] = v
        return s

class Fornitore(db.Model):
    __tablename__ = 'fornitore'
    id = db.Column(db.Integer, primary_key=True)
    # rm: categoria_fornitore_id = db.Column(db.Integer, db.ForeignKey('categoria_fornitore.id'))
    pagamento_id = db.Column(db.Integer, db.ForeignKey('pagamento.id'))
    pagamento = db.relationship('Pagamento')
    #rm: magazzino_id = db.Column(db.Integer, db.ForeignKey('magazzino.id'))

fornitore_magazzino = db.Table('fornitore_magazzino',
    db.Column('fornitore_id', db.Integer, db.ForeignKey('fornitore.id')),
    db.Column('magazzino_id', db.Integer, db.ForeignKey('magazzino.id')))

fornitore_categoria_fornitore = db.Table('fornitore_categoria_fornitore',
    db.Column('fornitore_id', db.Integer, db.ForeignKey('fornitore.id')),
    db.Column('categoria_fornitore_id', db.Integer, db.ForeignKey('categoria_fornitore.id')))

class Fornitura(db.Model):
    __tablename__ = 'fornitura'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime)
    prezzo_lordo = db.Column(db.Numeric(16,5))
    prezzo_netto = db.Column(db.Numeric(16,5))
    data_prezzo = db.Column(db.DateTime)
    numero_lotto = db.Column(db.String(80))
    data_scadenza = db.Column(db.DateTime)
    data_produzione = db.Column(db.DateTime)
    articolo_id = db.Column(db.Integer, db.ForeignKey('articolo.id', onupdate="CASCADE", ondelete="CASCADE"))
    articolo = db.relationship('Articolo')
    fornitore_id = db.Column(db.Integer, db.ForeignKey('fornitore.id', onupdate="CASCADE", ondelete="RESTRICT"))
    fornitore = db.relationship('Fornitore')

class Imballaggio(db.Model):
    __tablename__ = 'imballaggio'
    id = db.Column(db.Integer, primary_key=True)
    denominazione = db.Column(db.String(200), unique=True)

class Articolo(db.Model):
    __tablename__ = 'articolo'
    id = db.Column(db.Integer, primary_key=True)
    codice = db.Column(db.String(50))
    denominazione = db.Column(db.String(600))
    produttore = db.Column(db.String(150))
    lunghezza = db.Column(db.Float)
    larghezza = db.Column(db.Float)
    altezza = db.Column(db.Float)
    volume = db.Column(db.String(20))
    unita_peso = db.Column(db.String(20))
    quantita_minima = db.Column(db.Float)
    immagine = db.Column(db.LargeBinary)

    categoria_articolo_id = db.Column(db.Integer, db.ForeignKey('categoria_articolo.id'))
    categoria_articolo = db.relationship('CategoriaArticolo')

    aliquota_iva_id = db.Column(db.Integer, db.ForeignKey('aliquota_iva.id'))
    aliquota_iva = db.relationship('AliquotaIva')

    imballaggio_id = db.Column(db.Integer, db.ForeignKey('imballaggio.id'))
    imballaggio = db.relationship('Imballaggio')

class Listino(db.Model):
    __tablename__ = 'listino'
    id = db.Column(db.Integer, primary_key=True)
    denominazione = db.Column(db.String(200))
    descrizione = db.Column(db.Text)
    data_creazione = db.Column(db.DateTime)
    nascosto = db.Column(db.Boolean, default=False)
    sospeso = db.Column(db.Boolean, default=False)

class ListinoArticolo(db.Model):
    __tablename__ = 'listino_articolo'    
    listino_id = db.Column(db.Integer, db.ForeignKey('listino.id'), primary_key=True)
    articolo_id = db.Column(db.Integer, db.ForeignKey('articolo.id'), primary_key=True)
    prezzo_dettaglio = db.Column(db.Numeric(16,5))
    prezzo_ingrosso = db.Column(db.Numeric(16,5))
    costo_ultimo = db.Column(db.Numeric(16,5))
    data = db.Column(db.DateTime)
    attuale = db.Column(db.Boolean, default=True)
    db.CheckConstraint("prezzo_dettaglio is not NULL OR prezzo_ingrosso is not NULL")

class Ordine(db.Model):
    __tablename__ = 'ordine'
    id = db.Column(db.Integer, primary_key=True)
    #name = db.Column(db.Unicode(255))
    prezzo = db.Column(db.Numeric)
    fatturato = db.Column(db.Boolean, default=False)
    # Fornitore o cliente
    attore_type = db.Column(db.String(255))
    attore_id = db.Column(db.Integer)
    attore = generic_relationship(attore_type, attore_id)

class Documento(db.Model):
    __tablename__ = 'documento'
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, nullable=False)
    parte = db.Column(db.Integer, default=1)
    data_documento = db.Column(db.DateTime)
    data_inserimento = db.Column(db.DateTime, default=datetime.utcnow())
    causale_trasporto = db.Column(db.String(100))
    aspetto_esteriore_beni = db.Column(db.String(100))
    # Testata documento o movimento
    #tipo_testata_type = db.Column(db.String(255))
    #tipo_testata_id = db.Column(db.Integer)
    #tipo_testata = generic_relationship(tipo_testata_type, tipo_testata_id)
    # Fornitore o cliente
    attore_type = db.Column(db.String(255))
    attore_id = db.Column(db.Integer)
    attore = generic_relationship(attore_type, attore_id)
    db.CheckConstraint('attore_id IS NOT NULL AND attore_type IS NOT NULL')

class Riga(db.Model):
    __tablename__ = 'riga'
    id = db.Column(db.Integer, primary_key=True)
    descrizione = db.Column(db.String(500))
    quantita = db.Column(db.Numeric(16,5))
    #
    aliquota_iva_id = db.Column(db.Integer, db.ForeignKey('aliquota_iva.id', onupdate="CASCADE", ondelete="RESTRICT"))
    aliquota_iva = db.relationship('AliquotaIva')
    articolo_id = db.Column(db.Integer, db.ForeignKey('articolo.id', onupdate="CASCADE", ondelete="RESTRICT"))
    articolo = db.relationship('Articolo')
    listino_id = db.Column(db.Integer, db.ForeignKey('listino.id', onupdate="CASCADE", ondelete="RESTRICT"))
    listino = db.relationship('Listino')

class RigaDocumento(db.Model):
    __tablename__ = 'riga_documento'
    riga_id = db.Column(db.Integer, db.ForeignKey('riga.id'), primary_key=True)
    documento_id = db.Column(db.Integer, db.ForeignKey('documento.id'), primary_key=True)


# Setup Flask-Restless
from flask.ext.restless import APIManager
app.manager = APIManager(app, flask_sqlalchemy_db=db)
app.manager.create_api(Documento, methods=['GET', 'POST', 'DELETE'])