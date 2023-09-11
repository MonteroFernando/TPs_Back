from ..models.film_model import Film
from ..models.exceptions import FilmNotFound, InvalidDataError

from flask import request

from decimal import Decimal

class FilmController:
    """Film controller class"""

    @classmethod
    def get(cls, film_id):
        """Get a film by id"""
        film = Film(film_id=film_id)
        result = Film.get(film)
        if result is not None:
            return result.serialize(), 200
        else:
            raise FilmNotFound(film_id)
        
    @classmethod
    def get_all(cls):
        """Get all films"""
        film_objects = Film.get_all()
        films = []
        for film in film_objects:
            films.append(film.serialize())
        return films, 200
    
    @classmethod
    def create(cls):
        """Create a new film"""
        data = request.json
        # TODO: Validate data
        if len(data.get('title'))<3:
            raise InvalidDataError('title')
        
        if not isinstance(data.get('language_id'), int):
            raise InvalidDataError('language_id')
        
        if not isinstance(data.get('rental_duration'), int):
            raise InvalidDataError('rental_duration')
        
        if data.get('rental_rate') is not None:
            if isinstance(data.get('rental_rate'), int):
                data['rental_rate'] = Decimal(data.get('rental_rate'))/100
            else:
                raise InvalidDataError('rental_rate')
        
        if data.get('replacement_cost') is not None:
            if isinstance(data.get('replacement_cost'), int):
                data['replacement_cost'] = Decimal(data.get('replacement_cost'))/100
            else:
                raise InvalidDataError('replacement_cost')
        
        if not isinstance(data.get('special_features'),list):
            raise InvalidDataError('special_features')
        else:
            primary_set={'Trailers','Commentaries', 'Deleted Scenes', 'Behind the Scenes'}
            secundary_set=set(data.get('special_features'))
            #compruebo con funcion all() si todos los elmentos de special_feature son str
            if not all(isinstance(feature,str) for feature in secundary_set):
                raise InvalidDataError('special_features')
            #compruebo que no haya otro elemento no permitido en special_features
            if not secundary_set.issubset(primary_set):
                raise InvalidDataError('special_features')


        film = Film(**data)
        Film.create(film)
        return {'message': 'Film created successfully'}, 201

    @classmethod
    def update(cls, film_id):
        """Update a film"""
        data = request.json
        # TODO: Validate data
        if len(data.get('title'))<3:
            raise InvalidDataError('title')
        
        if not isinstance(data.get('language_id'), int):
            raise InvalidDataError('language_id')
        
        if not isinstance(data.get('rental_duration'), int):
            raise InvalidDataError('rental_duration')
        
        if data.get('rental_rate') is not None:
            if isinstance(data.get('rental_rate'), int):
                data['rental_rate'] = Decimal(data.get('rental_rate'))/100
            else:
                raise InvalidDataError('rental_rate')
        
        if data.get('replacement_cost') is not None:
            if isinstance(data.get('replacement_cost'), int):
                data['replacement_cost'] = Decimal(data.get('replacement_cost'))/100
            else:
                raise InvalidDataError('replacement_cost')
        
        if not isinstance(data.get('special_features'),list):
            raise InvalidDataError('special_features')
        else:
            primary_set={'Trailers','Commentaries', 'Deleted Scenes', 'Behind the Scenes'}
            secundary_set=set(data.get('special_features'))
            #compruebo con funcion all() si todos los elmentos de special_feature son str
            if not all(isinstance(feature,str) for feature in secundary_set):
                raise InvalidDataError('special_features')
            #compruebo que no haya otro elemento no permitido en special_features
            if not secundary_set.issubset(primary_set):
                raise InvalidDataError('special_features')
        
        
        data['film_id'] = film_id

        film = Film(**data)

        # TODO: Validate film exists
        if Film.exsist(film):
            Film.update(film)
            return {'message': 'Film updated successfully'}, 200
        else:
            raise FilmNotFound(film_id)
        
    @classmethod
    def delete(cls, film_id):
        """Delete a film"""
        film = Film(film_id=film_id)

        # TODO: Validate film exists
        if Film.exsist(film):
            Film.delete(film)
            return {'message': 'Film deleted successfully'}, 204
        else:
            raise FilmNotFound(film_id)