from openerp import models, fields

class ObjectFaculty(models.Model):
    _name = 'object.faculty'

    name = fields.Char('Faculty Name')
    faculty_id = fields.Char('Faculty ID')
