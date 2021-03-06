import {Component, OnInit} from 'angular2/core'
import {RouteConfig, ROUTER_DIRECTIVES, ROUTER_PROVIDERS } from 'angular2/router'
import {CategoryService} from './category.service'
import {CardService} from './card.service'
import {Category} from './card'
import {CardsComponent} from './cards.component'
import {CardComponent} from './card.component'

@Component({
    selector: 'app',
    template: `
	<select [(ngModel)]="selectedCategory">
        <option *ngFor="#category of categories" [ngValue]="category">{{category.name}}</option>
        </select>
	<nav>
	<a [routerLink]="['Cards']">Cards</a>
	<a [routerLink]="['Newcard']">Add Card</a>
	</nav>
	<router-outlet></router-outlet>
	`,
    directives: [ROUTER_DIRECTIVES],
    providers: [
	ROUTER_PROVIDERS,
	CardService,
	CategoryService
    ]
})

@RouteConfig([
    {
	path: '/cards',
	name: 'Cards',
	component: CardsComponent
    },
    {
	path: '/card',
	name: 'Newcard',
	component: CardComponent
    },
        {
	path: '/card/:id',
	name: 'Card',
	component: CardComponent
    }

])

export class AppComponent implements OnInit {
    ngOnInit() {
    	this.getCategories()
	this.selectedCategory = this.catInit[0]
	this.categories = this.catInit
    }
    constructor(private _categoryService: CategoryService){}
    categories: Category[]
    selectedCategory: Category
    catInit : Category[] = [
	{"id":0, "name": "All"},
	{"id":1, "name": "Unspecified"}
    ]
    onSelect(category: Category) {
    	this.selectedCategory = category
    }
    getCategories() {
    	this._categoryService.getCategories().then(categories => this.categories.push.apply(this.categories,categories))
    }
}
