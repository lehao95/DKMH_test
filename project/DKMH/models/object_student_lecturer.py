# -*- coding: utf-8 -*-
from openerp import models, fields


class ObjectStudentLecturer(models.Model):
    _name = 'object.student.lecturer'
    _inherit = 'res.partner'

    birth_date = fields.Date('Birth Date')
    student = fields.Boolean('Student', default=False)
    lecturer = fields.Boolean('Lecturer', default=False)
    student_id = fields.Integer(string='Student ID')
    faculty_id = fields.Many2one('object.faculty', 'Faculty')
    course_id = fields.Many2one('object.course', 'Course')


