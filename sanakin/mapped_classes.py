import os

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import relationship

from .corpus_file import BaseCorpusFile
from .corpus import BaseCorpus
from .sentence_delimiter import BaseSentenceDelimiter
from .corpus_data import BaseCorpusData
from .sentence import BaseSentence
from .morpheme import BaseMopheme

Base = automap_base()

class Corpus(Base, BaseCorpus):
    __tablename__ = 'corpora'
    corpus_files = relationship('CorpusFile')

    def extract_data(self, line):
        func = self._extract_function(self.corpus_id)
        return func(line)

class CorpusFile(Base, BaseCorpusFile):
    __tablename__ = 'corpus_files'

    def readline(self, dir_):
        '''
        Args:
            dir_[pathlib.Path]
        '''
        file_path_ = dir_.joinpath(self.corpus_file_id)
        for line in self._readline(file_path_):
            yield line

class CorpusData(Base, BaseCorpusData):
    __tablename__ = 'corpus_datum'
    # sentences = relationship('Sentence')

class SentenceDelimiter(Base, BaseSentenceDelimiter):
    __tablename__ = 'sentence_delimiters'

    def split(self, text):
        for sentence in self._split(self.regex, text):
            yield {
                'sentence_delimiter_id': self.sentence_delimiter_id,
                **sentence,
            }

class Sentence(Base, BaseSentence):
    __tablename__ = 'sentences'

class Morpheme(Base, BaseMopheme):
    __tablename__ = 'morphemes'

#
# class SplitMethod(Base):
#     __tablename__ = 'split_methods'
#     sentences = relationship('Sentence')
