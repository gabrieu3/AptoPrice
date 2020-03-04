from src.dto.ApDto import ApDto


class ApDao:

    @staticmethod
    def get_id():
        dto = ApDto('Gabriel')
        return dto.get_id()
