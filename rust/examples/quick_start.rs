use crawlora_jumia::{Client, JumiaCountriesParams, ModelJumiaCountriesResponseDoc};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client.jumia.countries(Default::default()).await?;
    let data: ModelJumiaCountriesResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
