import {Injectable} from 'angular2/core'
import {CATEGORIES} from './mock-categories'
import {Category} from './card'

@Injectable()
export class CategoryService {
    getCategories(){
	return Promise.resolve(CATEGORIES)
    }
}
