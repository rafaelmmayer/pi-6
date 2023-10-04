<script>
    import { onMount } from "svelte";

    let message;
    let inputText;
    let inputRes;

    async function clickBtnHandler() {
        const res = await fetch(`http://localhost:8000?frase=${inputText}`);
        const json = await res.json();
        inputRes = json.message;
    }

    onMount(async () => {
        const res = await fetch(
            "http://localhost:8000?frase=asodhasijdnhasuidbas"
        );
        const json = await res.json();

        message = json.message;
    });
</script>

<h1>{message ?? "Carregando"}</h1>
<input bind:value={inputText} />
<button on:click={clickBtnHandler}>Click</button>
<p>{inputRes ?? "manda o click, porra!!"}</p>
