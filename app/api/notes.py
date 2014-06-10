from datetime import datetime
from bson import ObjectId
from flask import jsonify, abort, request
from app import model

from app.api import api_requests
from app.auth import login


@api_requests.route('/notes', methods=['GET'])
@login.login_required
def get_all_notes():
    user_obj = model.User.objects(username=login.username())[0]

    if model.Note.objects(author=user_obj).count == 0:
        return jsonify({
            'success': True,
            'message': 'List of notes.',
            'data': []
            })

    notes = [note.to_mongo() for note in model.Note.objects(author=user_obj)]

    for note in notes:
        note['note_id'] = str(note['_id'])
        del note['_id']
        note['creation_time'] = int(note['creation_time'].strftime("%s")) * 1000
        note['modification_time'] = int(note['modification_time'].strftime("%s")) * 1000
        del note['body']
        del note['author']

    return jsonify({
        'success': True,
        'message': 'List of notes.',
        'data': notes
        })


@api_requests.route('/notes/<note_id>', methods=['GET'])
@login.login_required
def get_note(note_id):
    user_obj = model.User.objects(username=login.username())[0]

    if not ObjectId.is_valid(note_id):
        abort(404)
    if not model.Note.objects(pk=note_id, author=user_obj):
        abort(404)

    note = model.Note.objects(pk=note_id, author=user_obj)[0].to_mongo()

    note['note_id'] = str(note['_id'])
    del note['_id']
    note['creation_time'] = int(note['creation_time'].strftime("%s")) * 1000
    note['modification_time'] = int(note['modification_time'].strftime("%s")) * 1000
    del note['author']

    return jsonify({
        'success': True,
        'message': 'One note.',
        'data': note
        })


@api_requests.route('/notes', methods=['POST'])
@login.login_required
def make_note():
    user_obj = model.User.objects(username=login.username())[0]

    try:
        body = request.json['body']
        subject = request.json['subject']
    except:
        abort(400)

    if len(subject) == 0:
        subject = 'New note'

    model.Note(author = user_obj,
        body=body,
        subject=subject,
        creation_time=datetime.now(),
        modification_time = datetime.now()).save()

    return jsonify({
        'success': True,
        'message': 'Note was added.',
        'data': None
        })


@api_requests.route('/notes/<note_id>', methods=['PUT'])
@login.login_required
def edit_note(note_id):
    user_obj = model.User.objects(username=login.username())[0]

    if not ObjectId.is_valid(note_id):
        abort(400)
    if not model.Note.objects(pk=note_id, author=user_obj):
        abort(404)

    try:
        body = request.json['body']
        subject = request.json['subject']
    except:
        abort(400)

    if body != '':
        model.Note.objects(pk=note_id, author=user_obj)[0].update(set__body=body)
    if subject != '':
        model.Note.objects(pk=note_id, author=user_obj)[0].update(set__subject=subject)

    model.Note.objects(pk=note_id, author=user_obj)[0].update(set__modification_time=datetime.now())

    return jsonify({
        'success': True,
        'message': 'Note was edited',
        'data': None
        })


@api_requests.route('/notes/<note_id>', methods=['DELETE'])
@login.login_required
def delete_note(note_id):
    user_obj = model.User.objects(username=login.username())[0]

    if not ObjectId.is_valid(note_id):
        abort(400)
    if not model.Note.objects(pk=note_id, author=user_obj):
        abort(404)

    model.Note.objects(pk=note_id, author=user_obj)[0].delete()

    return jsonify({
        'success': True,
        'message': 'Note was deleted',
        'data': None
        })