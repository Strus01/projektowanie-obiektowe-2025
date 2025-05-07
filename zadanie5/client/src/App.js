import Products from './components/Products';
import Payments from './components/Payments';

function App() {
  return (
    <div className="App">
      <header>
        <h1>Online Store</h1>
      </header>
      <main>
        <Products/>
        <hr />
        <Payments/>
      </main>
    </div>
  );
}

export default App;
