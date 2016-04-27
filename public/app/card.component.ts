import {Component, OnInit} from 'angular2/core'
import {RouteParams} from 'angular2/router'
import {Card} from './card'
import {CardService} from './card.service'

@Component ({
    selector: 'card',
    templateUrl: 'app/card.component.html'
})
export class CardComponent implements OnInit {
    card: Card
    constructor(
	private _cardService: CardService,
	private _routeParams: RouteParams){
    }

    ngOnInit() {
	let id = +this._routeParams.get('id')
	this._cardService.getCard(id).then(card => this.card = card)
    }

    editQuestion() {

    }
}
