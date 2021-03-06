import {CARDS} from './mock-cards';
import {Card} from './card';
import {Injectable} from 'angular2/core'

@Injectable()
export class CardService {
    getCards() {
	return Promise.resolve(CARDS)
    }
    getCard(id: number) {
	return Promise.resolve(CARDS).then(
	    cards => cards.filter(card => card.id === id)[0]
	)
    }
    getCardsSlowly() {
	return new Promise<Card[]>(resolve => setTimeout(()=>resolve(CARDS), 2000))
    }
}
