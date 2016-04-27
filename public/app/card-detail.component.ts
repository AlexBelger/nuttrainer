import {Component, Input} from 'angular2/core'
import {Card} from './card';

@Component({
    selector: 'card-detail',
    template: `
	<div *ngIf="card">
	<div><label>{{card.category.name}}</label></div>
	<div>
	<label>name: </label>
	<input [(ngModel)]="card.first" placeholder="question"/>
	</div>
	</div>
	`
})

export class CardDetailComponent {
    @Input()
    card: Card
}








