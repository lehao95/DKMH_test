from openerp import models, fields

class ObjectCourse(models.Model):
    _name = 'object.course'

    name = fields.Char('Course Name')
    course_id = fields.Char('Course ID')
