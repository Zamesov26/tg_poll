from repositories.subject import SubjectRepository


class UnitOfWork:
    def __init__(self, session):
        self.session = session
        self.subject = SubjectRepository(session)

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()
