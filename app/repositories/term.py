from sqlalchemy.orm import Session

from app.models import Term


class TermRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return self.session \
            .query(Term) \
            .all()

    def get_by_id(self, term_id):
        return self.session \
            .query(Term) \
            .filter_by(id=term_id) \
            .first()

    def get_all_by_name(self, term_name):
        return self.session \
            .query(Term) \
            .filter_by(name=term_name) \
            .all()

    def get_or_create(self, name, section):
        for term in self.get_all_by_name(name):
            if term.subject_section is section:
                return term

        term = Term(name=name)
        section.terms.append(term)
        self.session.add(term)

        return term
